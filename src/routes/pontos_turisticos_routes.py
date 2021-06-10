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
from controllers import usuario_controller
from controllers import medalha_controller


# Rota /api/candango/attractions - Métodos GET
# @login_required - Necessário enviar cookie com sessão válida (autenticação do usuário /api/candango/attractions) 
# ["GET"] para buscar informações de todos os pontos turísticos
@candango_routes.route('/api/candango/attractions', methods=['GET'])
@login_required
def candango_lista_pontos_turisticos():
    if request.method == 'GET':
        pontosTuristicos = db.session.query(PontoTuristico).join(Local).all()
        listaPontosTuristicos = {"pontos turisticos" : []}
        for pontoTuristico in pontosTuristicos:
            listaPontosTuristicos["pontos turisticos"].append(pontoTuristico.toDict())
        print(listaPontosTuristicos)
        return listaPontosTuristicos, 200

            

        