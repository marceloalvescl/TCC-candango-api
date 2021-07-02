from smtplib import SMTP
from app import db
from models.usuario import Usuario
from controllers import attraction_controller, usuario_controller
from utils.builders import build_response_usuario, build_response_login, build_response, email_message_template
from settings import logger

from flask import send_file
from flask_login import login_user, current_user, logout_user
from passlib.context import CryptContext
from utils import bytesToImg
import sqlalchemy
import random
import string 

pwd_ctxt = CryptContext(schemes=['bcrypt'], deprecated="auto")

def cadastrarUsuario(requestJson):
    hashedPassword = pwd_ctxt.hash(requestJson["password"])
    usuario = Usuario(
                eml_usuario=requestJson["email"], 
                pwd_usuario=hashedPassword,
                nme_usuario=requestJson["name"],
                tlf_usuario=requestJson["phone"],
                gen_usuario=requestJson["gender"],
                est_usuario=requestJson["state"],
                pais_usuario=requestJson["country"]
            )
    try:
        db.session.add(usuario)
        db.session.commit()
        attractions, status = attraction_controller.getAllAttractions()
        login_user(usuario)
        return build_response_login("Cadastro realizado com sucesso!", usuario, attractions, status) 
    except sqlalchemy.exc.IntegrityError as e:
        if(str(e).find('(psycopg2.errors.UniqueViolation)') != -1):
            
            response = {"error": "O email informado ja existe no banco"}
            return response, 409
        logger.fatal(40, e)
    

def logarUsuario(requestJson):
    email = requestJson['email']
    usuario = Usuario.query.filter(
        Usuario.eml_usuario.like(email),
        Usuario.status_usuario == True
    ).first()
    if usuario:
        verifyHash = pwd_ctxt.verify(requestJson["password"], usuario.pwd_usuario)
        if( verifyHash):
            logger.info("Logando usuário: " + usuario.eml_usuario)
            login_user(usuario)
            attractions, status = attraction_controller.getAllAttractions()
            return build_response_login("Usuário logado!", usuario, attractions, status)
        elif(usuario.status_usuario == False):
            return {'error' : 'Esta conta está desativada!'}
        elif(not verifyHash):
            response = {"error": "Usuário ou senha inválidos"}
            return response, 401
    else:
        response = {"error": "Usuário ou senha inválidos"}
        return response, 401

def deslogarUsuario():
    logout_user()
    response = {"Sucesso": "Logout realizado com sucesso"}
    return response, 201

def esqueceuSenha(requestJson):
    try:
        email = requestJson['email']
        usuario = Usuario.query.filter(
            Usuario.eml_usuario.like(email)
        ).first()
        content, status = enviarCodigoRecuperacaoSenha(usuario)
        return content, status
    except KeyError as e :
        logger.fatal(e)
        content = {"error" : "Fornecer email!"}
        status = 400
        return content, status

def enviarCodigoRecuperacaoSenha(usuario):
    with SMTP('smtp.gmail.com') as smtp:
        try: 
            gerarCodigoRecuperarSenha(usuario)
            smtp.ehlo()
            smtp.starttls()
            smtp.login("candangoapp@gmail.com","Candango2021")
            email = usuario.eml_usuario
            usuario = Usuario.query.filter(
                Usuario.eml_usuario.like(email)
            ).first()
            msg = email_message_template(usuario)
            smtp.sendmail("candangoapp@gmail.com", usuario.eml_usuario, msg)
            smtp.quit()
            status = 200
            response = {"sucesso": "Email com código de redefinição enviado!"}
            return response, status
            
        except Exception as e:
            status = 400
            response = {"error": "Email inexistente"}
            return response, status

def gerarCodigoRecuperarSenha(usuario):
    codRecuperarSenha = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    usuario.cod_recuperar_senha = codRecuperarSenha
    db.session.add(usuario)
    db.session.commit()
    db.session.refresh(usuario)
    logger.info("Código de recuperar senha gerado" + str(usuario))
    return "Código de recuperar senha gerado!" +  str(usuario)
    
def alterarSenha(requestJson):
    try:
        email = requestJson['email']
        newHashedPassword = pwd_ctxt.hash(requestJson['newpassword'])
        codRecuperarSenha = requestJson['recoverycode']
        usuario = Usuario.query.filter(
            Usuario.eml_usuario.like(email),
            Usuario.cod_recuperar_senha.like(codRecuperarSenha)
        ).first()
        usuario.pwd_usuario = newHashedPassword
        db.session.add(usuario)
        db.session.commit()
        return build_response_usuario("Senha alterada com sucesso", usuario), 200
    except Exception as e :
        logger.fatal(e)
        content = {"error": "Email ou código de redefinir senha inválido"}
        content = content
        status = 401
    return build_response(content, status)

def informacoesUsuarioLogado():
    usuario = current_user
    logger.info("Informações do usuário: " + usuario.eml_usuario)
    return build_response_usuario("Encontrado", current_user), 201

def alterarSenhaUsuarioLogado(requestJson):
    if (pwd_ctxt.verify(requestJson["oldPassword"], current_user.pwd_usuario)):
        current_user.pwd_usuario = pwd_ctxt.hash(requestJson['newPassword'])
        db.session.add(current_user)
        db.session.commit()
        attractions, status = attraction_controller.getAllAttractions()
        return build_response_login("Dados alterados com sucesso", current_user, attractions, status)
    else:
        return {'error' : 'Senha atual informada está incorreta!'}, 401

def alterarInfoUsuario(requestJson):
    try:
        logger.info(requestJson)
        usuario = current_user
        
        usuario.nme_usuario = requestJson["name"]
        #usuario.eml_usuario = requestJson["email"]
        usuario.tlf_usuario = requestJson["phone"]
        usuario.gen_usuario = requestJson["gender"]
        usuario.est_usuario = requestJson["state"]
        usuario.pais_usuario = requestJson["country"]
        
        logger.info(current_user.pwd_usuario)
        db.session.add(usuario)
        db.session.commit()

        attractions, status = attraction_controller.getAllAttractions()
        return build_response_login("Dados alterados com sucesso", usuario, attractions, status)
    except KeyError as e :
        logger.fatal(e)
        content = {"error": "JSON incorreto"}
        status = 404
        return content, status
    except Exception as e:
        logger.fatal(e)
        content = {"error" : str(e)}
        status = 504
        return content, status

def setImagemPerfil(file):
    try:
        current_user.bytea_fto_conta = file.read()
        db.session.add(current_user)
        db.session.commit()
        return {'msg' : 'Imagem de perfil adicionada'}, 200
    except Exception as e:
        return {'msg': 'Algo deu errado, contate o suporte'}, 500

def getImagemPerfil():
    bytes = current_user.bytea_fto_conta
    img_io = bytesToImg.bytesToPNG(bytes=bytes)
    return send_file(img_io, mimetype='image/png'), 200

def desativarContaUsuario():
    current_user.status_usuario = False
    db.add(current_user)
    db.commit()
    return {'msg' : 'Conta desativada'}, 200

def ativarContaUsuario():
    current_user.status_usuario = True
    db.add(current_user)
    db.commit()
    return {'msg' : 'Conta ativada'}, 200