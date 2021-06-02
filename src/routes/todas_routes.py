from models.tipo_turistico import TipoTuristico
from models.ponto_turistico import PontoTuristico
from flask import Blueprint, jsonify, request, current_app, send_file
from flask_login import login_user, logout_user, current_user, login_required
from flask_cors import CORS
from utils.builders import build_response_usuario, build_response
from settings import logger
import json
from models.usuario import Usuario
from models.ponto_turistico import PontoTuristico
from models.local import Local
import sqlalchemy
from app import db
from routes import candango_routes
from controllers import usuario_controller



@candango_routes.route('/api/candango/pontosTuristicos', methods=['GET'])
@login_required
def candango_lista_pontos_turisticos():
    if request.method == 'GET':
        pontosTuristicos = db.session.query(PontoTuristico).join(Local).all()
        listaJsonPontoTuristico = []
        for pontoTuristico in pontosTuristicos:
            listaJsonPontoTuristico.append(pontoTuristico.toJson())
        print(listaJsonPontoTuristico)
            
@candango_routes.route('/api/candango/imagem/<image>', methods=['GET'])
def candango_imagem(image):
    if request.method == 'GET':
        try:
            return send_file('D:\\TCC-candango-api\\src\\utils\\imagens\\{0}.jpg'.format(image), mimetype='image/jpg'), 200
        except Exception as e:
            content = '{"error" : "imagem inexistente!"}'
            status = 404
            return json.loads(content), status
        
@candango_routes.route('/api/candango/medalhasUsuario', methods=['POST'])
@login_required
def candango_medalhas_usuario():
    if request.method == 'POST':
        try:
            content, status = usuario_controller.medalhas()
        except Exception as e :
            logger.fatal(e)
            content = ""
            status = 504

    return build_response(content, status)