from smtplib import SMTP

import sqlalchemy
from app import db
from models.medalha import Medalha
from models.ponto_turistico import PontoTuristico
from models.usuario import Usuario
from models.usuario_medalha import UsuarioMedalha
from models.usuario_ponto_turistico import UsuarioPontoTuristico
from settings import logger
from flask_login import current_user
import json

def getMedalhas():
    medalhas = Medalha.query.all()
    print(medalhas)
    dict_medalhas = {}
    for medalha in medalhas:
        print(type(medalha))
        dict_medalhas['Id da medalha: ' + str(medalha.id_medalha)] = medalha.toDict()
    
    return dict_medalhas, 201

def getUserMedal():
    usuario = current_user
    dict_medalhas = {'medals':[]}
    todas_medalhas = Medalha.query.all()
    
    for medalha in todas_medalhas:
        dict_medalhas['medals'].append(medalha.toDict())
    
    print("Medalhas do usuário" + str(usuario.medalhas))
    for medalha in usuario.medalhas:
        
        indice = dict_medalhas['medals'].index(medalha.toDict())
        usuarioMedalha = db.session.query(UsuarioMedalha).filter(UsuarioMedalha.cod_usuario==current_user.id_usuario, 
                                                                UsuarioMedalha.cod_medalha==medalha.id_medalha
                                                                ).first()
        dict_medalhas['medals'][indice]['unlockDate'] = usuarioMedalha.dta_conquista_medalha
        dict_medalhas['medals'][indice]['hasMedal'] = True

    return dict_medalhas, 201

def setUserMedal(json):
    attractionCode = json['attractionCode']
    medalCode = db.session.query(Medalha).filter_by(cod_ponto_turistico=attractionCode).first().id_medalha
    
    #Verifica se usuário já liberou a medalha
    for medalha in current_user.medalhas:
        if(medalha.id_medalha == medalCode):
            return {"error" : "Usuário ja possui essa medalha"}

    #Verifica se usuário já visitou o ponto turístico dessa medalha
    userVisitedAttraction = False
    for attraction in current_user.attractions:
        if(attraction.id_ponto_turistico == attractionCode):
            userVisitedAttraction = True
    if (not userVisitedAttraction):
        return {"error" : "Usuário precisa visitar o ponto turístico para liberar medalha"}, 400        

    usuarioMedalhas = UsuarioMedalha(
        cod_usuario=current_user.id_usuario,
        cod_medalha=medalCode
    )
    db.session.add(usuarioMedalhas)
    db.session.commit()
    print(usuarioMedalhas)
    return {"success" : "Medalha adicionada ao usuário - " + current_user.nme_usuario}, 200

 
    