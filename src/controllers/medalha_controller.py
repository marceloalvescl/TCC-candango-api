from smtplib import SMTP
from app import db
from models.medalha import Medalha
from settings import logger
from flask_login import current_user
import json

def todas_medalhas():
    medalhas = Medalha.query.all()
    print(medalhas)
    dict_medalhas = {}
    for medalha in medalhas:
        print(type(medalha))
        dict_medalhas['Id da medalha: ' + str(medalha.id_medalha)] = medalha.toDict()
    
    return dict_medalhas, 201

def medalhas_usuario():
    usuario = current_user
    dict_medalhas = {'medals':[]}
    
    todas_medalhas = Medalha.query.all()
    for medalha in todas_medalhas:
        dict_medalhas['medals'].append(medalha.toDict())
    
    for medalha in usuario.medalhas:
        indice = dict_medalhas['medals'].index(medalha.toDict())
        if indice != 1:
            dict_medalhas['medals'][indice]['hasMedal'] = True

    return dict_medalhas, 201
