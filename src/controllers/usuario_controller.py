from smtplib import SMTP
from app import db
from models.usuario import Usuario
from utils.builders import build_response_usuario
from utils.builders import build_response
from settings import logger

from flask_login import login_user, current_user
import sqlalchemy
import random
import string 
import json

def cadastrarUsuario(requestJson):
    usuario = Usuario(
                eml_usuario=requestJson["email"], 
                pwd_usuario=requestJson["password"], 
                nme_usuario=requestJson["name"],
                tlf_usuario=requestJson["phone"],
                gen_usuario=requestJson["gender"],
                est_usuario=requestJson["state"],
                pais_usuario=requestJson["country"]
            )
    try:
        db.session.add(usuario)
        db.session.commit()
        return build_response_usuario("Cadastro realizado com sucesso!", usuario), 200 
    except sqlalchemy.exc.IntegrityError as e:
        if(str(e).find('(psycopg2.errors.UniqueViolation)') != -1):
            
            response = '{"error": "O email informado ja existe no banco"}'
            return json.loads(response), 409
        logger.fatal(40, e)

def logarUsuario(requestJson):
    email = requestJson['email']
    senha = requestJson['password']
    usuario = Usuario.query.filter(
        Usuario.eml_usuario.like(email),
        Usuario.pwd_usuario.like(senha)
    ).first()
    if(usuario):
        logger.info("Logando usuário: " + usuario.eml_usuario)
        login_user(usuario)
        response = '{"sucesso": "Usuário logado"}'
        return json.loads(response), 201
    else:
        response = '{"error": "Usuário ou senha inválidos"}'
        return json.loads(response), 401

def esqueceuSenha(requestJson):
    try:
        email = requestJson['email']
        usuario = Usuario.query.filter(
            Usuario.eml_usuario.like(email)
        ).first()
        content, status = enviarCodigoRecuperacaoSenha(usuario)
        return json.loads(content), status
    except KeyError as e :
        logger.fatal(e)
        content = '{"error" : "Fornecer email!"}'
        status = 400
        return json.loads(content), status

def enviarCodigoRecuperacaoSenha(usuario):
    with SMTP('smtp.gmail.com') as smtp:
        try: 
            resultado = gerarCodigoRecuperarSenha(usuario)
            print(resultado)
            smtp.ehlo()
            smtp.starttls()
            smtp.login("candangoapp@gmail.com","Candango2021")
            email = usuario.eml_usuario
            usuario = Usuario.query.filter(
                Usuario.eml_usuario.like(email)
            ).first()
            msg = usuario.cod_recuperar_senha
            smtp.sendmail("candangoapp@gmail.com", usuario.eml_usuario, msg)
            smtp.quit()
            status = 200
            response = '{"sucesso": "Email com código de redefinição enviado!"}'
            
        except Exception as e:
            print(e)
            status = 400
            response = '{"error": "Email inexistente"}'
        return response, status

def gerarCodigoRecuperarSenha(usuario):
    print(type(usuario))
    print(usuario)
    codRecuperarSenha = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(6))
    usuario.cod_recuperar_senha = codRecuperarSenha
    
    try:
        db.session.add(usuario)
        db.session.commit()
        logger.info("Código de recuperar senha gerado" + str(usuario))
        return "Código de recuperar senha definido!" +  str(usuario)
    except sqlalchemy.exc.IntegrityError as e:
        if(str(e).find('(psycopg2.errors.UniqueViolation)') != -1):
            return json.loads('"Erro": "O email informado ja existe no banco"'), 409
        logger.log(40, e)
    
def alterarSenha(requestJson):
    try:
        email = requestJson['email']
        novaSenha = requestJson['newpassword']
        codRecuperarSenha = requestJson['recoverycode']
        usuario = Usuario.query.filter(
            Usuario.eml_usuario.like(email),
            Usuario.cod_recuperar_senha.like(codRecuperarSenha)
        ).first()
        usuario.pwd_usuario = novaSenha
        db.session.add(usuario)
        db.session.commit()
        return build_response_usuario("Senha alterada com sucesso", usuario), 200
    except Exception as e :
        logger.fatal(e)
        content = '{"error": "Email ou código de redefinir senha inválido"}'
        content = json.loads(content)
        status = 401
    return build_response(content, status)

def informacoesUsuarioLogado():
    usuario = current_user
    logger.info("Informações do usuário: " + usuario.eml_usuario)
    return build_response_usuario("Encontrado", current_user), 201

def alterarInfoUsuario(requestJson):
    try:
        usuario = current_user
        if(usuario):
            usuario.nme_usuario = requestJson["email"]
            usuario.eml_usuario = requestJson["name"]
            usuario.tlf_usuario = requestJson["phone"]
            usuario.gen_usuario = requestJson["gender"]
            usuario.est_usuario = requestJson["state"]
            usuario.pais_usuario = requestJson["country"]
            db.session.add(usuario)
            db.session.commit()
            return build_response_usuario("Dados alterados com sucesso", usuario), 200
            
    except KeyError as e :
        logger.fatal(e)
        content = '{"error": "JSON incorreto"}'
        status = 404
        return json.loads(content), status
    except Exception as e:
        logger.fatal(e)
        content = '{"error" : "{}"}'.format(e)
        status = 504
        return json.loads(e, status)

def medalhas():
    usuario = current_user
    medalhas = usuario.medalhas
    for x in medalhas:
        print(x.nme_medalha)
    logger.info(usuario.medalhas)
    return build_response("Medalhas: {0}".format(usuario.medalhas), 201)