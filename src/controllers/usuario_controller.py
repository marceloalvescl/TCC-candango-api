from smtplib import SMTP
from app import db
from models.usuario import Usuario
from utils.builders import build_response_usuario
from settings import logger
import sqlalchemy
import random
import string 
import json

def forgotPassword(usuario):
    with SMTP('smtp.gmail.com') as smtp:
        try: 
            resultado = gerarCodigoRecuperarSenha(usuario)
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
        return build_response_usuario("Cadastro realizado com sucesso!", usuario), 200 
    except sqlalchemy.exc.IntegrityError as e:
        if(str(e).find('(psycopg2.errors.UniqueViolation)') != -1):
            return json.loads('"Erro": "O email informado ja existe no banco"'), 409
        logger.log(40, e)
    
def changePassword(usuario, novaSenha):
    usuario.pwd_usuario = novaSenha
    db.session.add(usuario)
    db.session.commit()
    return build_response_usuario("Senha alterada com sucesso", usuario), 200

def alterarUsuario(usuario):
    email = usuario.eml_usuario
    usuarioExiste = Usuario.query.filter(
        Usuario.eml_usuario.like(email)
    ).first()

    if(usuarioExiste):
        usuarioExiste.nme_usuario = usuario.nme_usuario
        usuarioExiste.eml_usuario = usuario.eml_usuario
        usuarioExiste.tlf_usuario = usuario.tlf_usuario
        usuarioExiste.gen_usuario = usuario.gen_usuario
        usuarioExiste.est_usuario = usuario.est_usuario
        usuarioExiste.pais_usuario = usuario.pais_usuario
        try:
            db.session.add(usuarioExiste)
            db.session.commit()
            return build_response_usuario("Dados alterados com sucesso", usuario), 200
        except Exception as e:
            logger.fatal(e)