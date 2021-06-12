from models.tipo_turistico import TipoTuristico
from models.ponto_turistico import PontoTuristico
from flask import Blueprint, jsonify, request, current_app, send_file
from flask_login import login_user, logout_user, current_user, login_required
from models.usuario import Usuario
from models.ponto_turistico import PontoTuristico
from models.local import Local
import sqlalchemy
from app import db
from routes import candango_routes
from controllers import usuario_controller, medalha_controller, attraction_controller
import json

# Rota /api/candango/attractions - Métodos GET
# @login_required - Necessário enviar cookie com sessão válida (autenticação do usuário /api/candango/user/signin) 
# ["GET"] para buscar informações de todos os pontos turísticos
@candango_routes.route('/attractions', methods=['GET'])
@login_required
def candango_lista_pontos_turisticos():
    if request.method == 'GET':
        return attraction_controller.getAllAttractions()

# Rota /api/candango/attractions/user - Métodos GET
# @login_required - Necessário enviar cookie com sessão válida (autenticação do usuário /api/candango/user/signin) 
# ["GET"] para buscar informações de todos os pontos turísticos visitados pelo usuário <attraction_controller.getUserVisitedAttractions>
# ["POST"] para adicionar visita ou incrementar visitas do usuário ao ponto turístico <attraction_controller.setUserVisitedAttraction>
@candango_routes.route('/attractions/user', methods=['GET', 'POST'])
@login_required
def candango_visited_attractions():
    if request.method == 'GET':
        return attraction_controller.getUserVisitedAttractions()
    if request.method == 'POST':
        if request.json:
            return attraction_controller.setUserVisitedAttraction(request.json)
        else:
            return json.loads('{"error" : "Favor enviar JSON na request"}'), 404             