from smtplib import SMTP
from app import db
from models.medalha import Medalha
from utils.builders import build_response_usuario
from utils.builders import build_response
from settings import logger


def todas_medalhas():
    medalhas = Medalha.query.all()
    print(medalhas)
    dict_medalhas = {}
    for medalha in medalhas:
        print(type(medalha))
        dict_medalhas['Id da medalha: ' + str(medalha.id_medalha)] = medalha.toDict()
    
    return dict_medalhas, 201
   