from app import db
from models.ponto_turistico import PontoTuristico
from models.usuario_ponto_turistico import UsuarioPontoTuristico
from models.local import Local
from models.level import Level
from controllers import medalha_controller, level_controller
from settings import logger
from utils import bytesToImg
from flask import send_file
from flask_login import current_user
from sqlalchemy  import func
import datetime

def getAllAttractions():
    pontosTuristicos = db.session.query(PontoTuristico).join(Local).all()
    listaPontosTuristicos = []
    for pontoTuristico in pontosTuristicos:
        listaPontosTuristicos.append(pontoTuristico.toDict())
    return listaPontosTuristicos, 200

def getAttractionById(attractionId):
    pontoTuristico = db.session.query(PontoTuristico).join(Local).filter(PontoTuristico.id_ponto_turistico == attractionId).first()
    return pontoTuristico

def getUserVistedAttraction(attractionId):
    userVisitedAttraction = db.session.query(UsuarioPontoTuristico).join(PontoTuristico).filter(
        UsuarioPontoTuristico.cod_usuario == current_user.id_usuario,
        UsuarioPontoTuristico.cod_ponto_turistico == attractionId
    ).first()
    return userVisitedAttraction

def getAllUserVisitedAttractions():
    usuario = current_user
    print(current_user.id_usuario)
    userVisitedAttractions = db.session.query(UsuarioPontoTuristico).join(PontoTuristico).filter(
        UsuarioPontoTuristico.cod_usuario == current_user.id_usuario
    ).all()
    dict_attractions = {'attractions':[]}
    print(userVisitedAttractions)
    for visitedAttraction in userVisitedAttractions:
        dict_attractions['attractions'].append(visitedAttraction.toDict())
    print(dict_attractions)

    return dict_attractions, 200

def setUserVisitedAttraction(json):
    attractionCode = json['attractionCode']
    
    attraction = db.session.query(PontoTuristico).filter(
        PontoTuristico.id_ponto_turistico == attractionCode
    ).first()

    level_controller.addExp(current_user, attraction.qtd_experiencia)

    userVisitedAttraction = db.session.query(UsuarioPontoTuristico).filter(
        UsuarioPontoTuristico.cod_ponto_turistico == attraction.id_ponto_turistico,
        UsuarioPontoTuristico.cod_usuario == current_user.id_usuario
    ).first()
    if(not userVisitedAttraction):
        usuarioPontoTuristico = UsuarioPontoTuristico(
            cod_usuario = current_user.id_usuario,
            cod_ponto_turistico=attraction.id_ponto_turistico,
            qtd_visitas = 1
        )
        db.session.add(usuarioPontoTuristico)
        db.session.add(current_user)
        db.session.commit()
        result, status = medalha_controller.setUserMedal(json)
        statusMedalha = f"Usuário já possui a medalha para o Ponto Turístico {attraction.nme_ponto_turistico}"
        if('success' in result):
            statusMedalha = result['success']
        return {
            "msg": "ponto turistico visitado!",
            "medalStatus" : statusMedalha,
            "exp" : current_user.qtd_exp_atual,
            "currentLevel" : level_controller.getLevelById(current_user.cod_level)
        }, status
    else:
        
        last_visit = userVisitedAttraction.dta_usuario_ponto_turistico
        current_time = datetime.datetime.now()
        difference =  current_time - last_visit
        logger.info("Última visita há: " + str(difference.days) + " dias")

        if(difference.days >= 1):
            userVisitedAttraction.dta_usuario_ponto_turistico = func.current_timestamp()
            userVisitedAttraction.qtd_visitas += 1
            db.session.add(userVisitedAttraction)
            db.session.commit() 
            msg = "ponto turistico visitado novamente!"
        else:
            msg = "Usuário já visitou esse ponto turístico nas últimas 24 horas!"


        return {
                "msg": msg,
                "exp" : current_user.qtd_exp_atual,
                "currentLevel" : level_controller.getLevelById(current_user.cod_level)
            }, 201

def setImagemAttraction(file, attractionId):
    try:
        attraction = getAttractionById(attractionId)
        attraction.bytea_fto_ponto_turistico = file.read()
        db.session.add(attraction)
        db.session.commit()
        return {'msg' : 'Imagem do ponto turístico adicionada'}, 201
    except Exception as e:
        return {'msg': 'Algo deu errado, contate o suporte'}, 500

def getImagemAttraction(attractionId):
    logger.info(attractionId)
    attraction = getAttractionById(attractionId)
    if not attraction.bytea_fto_ponto_turistico:
        logger.info(f'imagem inexistente para o ponto turistico de id {attractionId}')
        return {'msg' : f'imagem inexistente para o ponto turistico de id {attractionId}'}, 404
    bytes = attraction.bytea_fto_ponto_turistico
    img_io = bytesToImg.bytesToPNG(bytes=bytes)
    
    return send_file(img_io, mimetype='image/png'), 200