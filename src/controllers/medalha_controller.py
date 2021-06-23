from app import db
from models.medalha import Medalha
from models.usuario_medalha import UsuarioMedalha
from controllers import level_controller
from settings import logger
from flask_login import current_user
from flask import send_file

def getMedalhas():
    medalhas = Medalha.query.all()
    dict_medalhas = {}
    for medalha in medalhas:
        dict_medalhas['Id da medalha: ' + str(medalha.id_medalha)] = medalha.toDict()
    
    return dict_medalhas, 200

def getUserMedal():
    usuario = current_user
    dict_medalhas = {'medals':[]}
    todas_medalhas = Medalha.query.all()
    for medalha in todas_medalhas:
        dict_medalhas['medals'].append(medalha.toDict())
    for medalha in usuario.medalhas:
        indice = dict_medalhas['medals'].index(medalha.toDict())
        usuarioMedalha = db.session.query(UsuarioMedalha).filter(UsuarioMedalha.cod_usuario==current_user.id_usuario, 
                                                                UsuarioMedalha.cod_medalha==medalha.id_medalha
                                                                ).first()
        dict_medalhas['medals'][indice]['unlockDate'] = usuarioMedalha.dta_conquista_medalha
        dict_medalhas['medals'][indice]['hasMedal'] = True

    return dict_medalhas, 201

def setUserMedal(json):
    logger.info(json)
    attractionCode = json['attractionCode']
    logger.info(json['attractionCode'])
    try:
        medal = db.session.query(Medalha).filter_by(cod_ponto_turistico=attractionCode).first()
        logger.info(medal.id_medalha)
    except AttributeError as e:
        return { "error" : "não existe ponto turistico com esse id"}, 404

    #Verifica se usuário já liberou a medalha
    for medalha in current_user.medalhas:
        if(medalha.id_medalha == medal.id_medalha):
            return {"error" : "Usuário ja possui essa medalha"}, 409

    #Verifica se usuário já visitou o ponto turístico dessa medalha
    userVisitedAttraction = False
    for attraction in current_user.attractions:
        if(attraction.id_ponto_turistico == attractionCode):
            userVisitedAttraction = True

    if (not userVisitedAttraction):
        return {"error" : "Usuário precisa visitar o ponto turístico para liberar medalha"}, 400        

    usuarioMedalhas = UsuarioMedalha(
        cod_usuario=current_user.id_usuario,
        cod_medalha=medal.id_medalha
    )
    
    level_controller.addExp(current_user, medal.qtd_experiencia)
    db.session.add(usuarioMedalhas)
    db.session.commit()
    print(usuarioMedalhas)
    return {
        "success" : f"Parabéns, {current_user.nme_usuario}, você liberou a {medal.nme_medalha}"
    }, 201

def getMedalhaImagem(image):
    try:
        logger.info(image)
        return send_file(f'D:\\ambientes-candango\\producao-candango\\TCC-candango-api\\src\\utils\\imagens\\{image}.jpg', mimetype='image/jpg'), 200
    except Exception as e:
        logger.fatal(e)
        content = {"error" : "imagem inexistente!"}
        status = 404
        return content, status