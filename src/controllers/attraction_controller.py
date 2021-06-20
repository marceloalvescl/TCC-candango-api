from app import db
from models.ponto_turistico import PontoTuristico
from models.usuario_ponto_turistico import UsuarioPontoTuristico
from models.local import Local
from settings import logger
from flask_login import current_user
from sqlalchemy  import func
import datetime

def getAllAttractions():
    pontosTuristicos = db.session.query(PontoTuristico).join(Local).all()
    listaPontosTuristicos = []
    for pontoTuristico in pontosTuristicos:
        listaPontosTuristicos.append(pontoTuristico.toDict())
    print(listaPontosTuristicos)
    return listaPontosTuristicos, 200

def getUserVisitedAttractions():
    usuario = current_user
    print(current_user.id_usuario)
    userVisitedAttractions = db.session.query(UsuarioPontoTuristico).join(PontoTuristico).filter(
        UsuarioPontoTuristico.cod_usuario == current_user.id_usuario
    ).all()
    dict_attractions = {'attractions':[]}
    print(userVisitedAttractions)
    for visitedAttraction in userVisitedAttractions:
        print(visitedAttraction)
        visitedAttractionDict = visitedAttraction.toDict()
        dict_attractions['attractions'].append(visitedAttraction.toDict())
    print(dict_attractions)

    return dict_attractions, 201

def setUserVisitedAttraction(json):
    attractionCode = json['attractionCode']
    
    attraction = db.session.query(PontoTuristico).filter(
        PontoTuristico.id_ponto_turistico == attractionCode
    ).first()

    current_user.addExp(attraction.qtd_experiencia)

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
        return {"msg": "ponto turistico visitado!"}, 201
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
            return {"msg": "ponto turistico visitado novamente!"}, 201
        else:
            return {"msg": "Usuário já visitou esse ponto turístico nas últimas 24 horas!"}, 201
