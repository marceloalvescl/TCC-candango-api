from app import db
from models.ponto_turistico import PontoTuristico
from models.usuario_ponto_turistico import UsuarioPontoTuristico
from models.local import Local
from models.level import Level
from controllers import medalha_controller, level_controller, attraction_controller
from settings.settings import logger
from flask import send_file
from flask_login import current_user
from sqlalchemy  import func
import os
import datetime
from PIL import Image
import io

def getAllAttractions():
    pontosTuristicos = db.session.query(PontoTuristico).join(Local).all()
    listaPontosTuristicos = {'attractions': []}
    for pontoTuristico in pontosTuristicos:
        listaPontosTuristicos['attractions'].append(pontoTuristico.toDict())
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
    userVisitedAttractions = db.session.query(UsuarioPontoTuristico).join(PontoTuristico).filter(
        UsuarioPontoTuristico.cod_usuario == current_user.id_usuario
    ).all()
    dict_attractions = {'attractions':[]}
    for visitedAttraction in userVisitedAttractions:
        dict_attractions['attractions'].append(visitedAttraction.toDict())

    return dict_attractions, 200

def setUserVisitedAttraction(json):
    attractionCode = json['attractionCode']
    
    attraction = db.session.query(PontoTuristico).filter(
        PontoTuristico.id_ponto_turistico == attractionCode
    ).first()

    userVisitedAttraction = db.session.query(UsuarioPontoTuristico).filter(
        UsuarioPontoTuristico.cod_ponto_turistico == attraction.id_ponto_turistico,
        UsuarioPontoTuristico.cod_usuario == current_user.id_usuario
    ).first()
    attractions, _ = getAllAttractions()
    userVisitedAttractions, _ = attraction_controller.getAllUserVisitedAttractions()
    if(not userVisitedAttraction):
        userVisitedAttraction = UsuarioPontoTuristico(
            cod_usuario = current_user.id_usuario,
            cod_ponto_turistico=attraction.id_ponto_turistico,
            qtd_visitas = 1
        )
        db.session.add(userVisitedAttraction)
        db.session.add(current_user)
        db.session.commit()
        result, status = medalha_controller.setUserMedal(json)
        statusMedalha = f"Usuário já possui a medalha para o Ponto Turístico {attraction.nme_ponto_turistico}"
        expAmmount = attraction.qtd_experiencia
        if('success' in result):
            statusMedalha = result['success']
            expAmmount += 10
        
        userVisitedAttractions, _ = attraction_controller.getAllUserVisitedAttractions()
        level_controller.addExp(current_user, expAmmount)
        return {
            "msg": "ponto turistico visitado!",
            "medalStatus" : statusMedalha,
            "exp" : current_user.qtd_exp_atual,
            "expReceived" : expAmmount, 
            "currentLevel" : level_controller.getLevelById(current_user.cod_level),
            "userVisitedAttraction" : userVisitedAttractions['attractions'],
            "attractions" : attractions['attractions']
        }, status
    else:
        
        last_visit = userVisitedAttraction.dta_usuario_ponto_turistico
        current_time = datetime.datetime.now()
        difference =  current_time - last_visit
        logger.info("Última visita há: " + str(difference.days) + " dias")

        if(difference.days >= 1):
            
            userVisitedAttraction.dta_usuario_ponto_turistico = func.current_timestamp()
            last_visit = userVisitedAttraction.dta_usuario_ponto_turistico
            userVisitedAttraction.qtd_visitas += 1
            db.session.add(userVisitedAttraction)
            db.session.commit() 
            expAmmount = attraction.qtd_experiencia
            level_controller.addExp(current_user, attraction.qtd_experiencia)
            msg = "ponto turistico visitado novamente!"
        else:
            expAmmount = 0
            msg = "Usuário já visitou esse ponto turístico nas últimas 24 horas!"

        userVisitedAttractions, _ = attraction_controller.getAllUserVisitedAttractions()
        return {
                "msg": msg,
                "medalStatus" : "Você já liberou essa medalha!",
                "exp" : current_user.qtd_exp_atual,
                "expReceived" : expAmmount, 
                "currentLevel" : level_controller.getLevelById(current_user.cod_level),
                "userVisitedAttraction" : userVisitedAttractions['attractions'],
                "attractions" : attractions['attractions']
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
    try:
        pil_img = Image.open(io.BytesIO(attraction.bytea_fto_ponto_turistico))
        img_io = io.BytesIO()
        pil_img.save(img_io, 'JPEG', quality=70)
        img_io.seek(0)
        
        return send_file(img_io, mimetype='image/jpeg', download_name=attraction.nme_ponto_turistico, as_attachment=True, attachment_filename= attraction.nme_ponto_turistico + '.jpg')
    except (FileNotFoundError, AttributeError):
        return {'error' : 'Imagem não encontrada'}

