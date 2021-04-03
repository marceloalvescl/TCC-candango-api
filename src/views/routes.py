from flask import Blueprint, jsonify, request, current_app
from flask_cors import CORS
from utils.builders import build_response
from settings import logger
from controllers.usuario_controller import UsuarioController

candango_routes = Blueprint('candango', __name__)
CORS(candango_routes)




class Routes:

    @candango_routes.route('/api/candango/signup',
                        methods=['POST'])
    def candango_signup():
        if request.method == 'POST':
            if request.json: 
                print(request.json)
                content, status = UsuarioController().signup(request.json)

        return build_response(content, status)

    @candango_routes.route('/api/candango/signin',
                        methods=['POST'])
    def candango_singin():
        if request.method == 'POST':
            if request.json: 
                content, status = UsuarioController().login(request.json)
            else:
                content = "Fornecer usuário e senha!"
                status = 400

        return build_response(content, status)

    @candango_routes.route('/api/candango/usuario',
                        methods=['GET'])
    def candango_usuario():
        if request.method == 'GET':
            try:
                content, status = candango_get_usuario(request.json)
            except Exception as e :
                print(e)
                content = ""
                status = 504
        
        return build_response(content, status)

    @candango_routes.route('/api/candango/forgot_password', methods=['POST'])
    def candango_forgot_password():
        if request.method == 'POST':
            try:
                content, status = UsuarioController().forgot_password(request.json)
            except Exception as e :
                logger.fatal(e)
                content = ""
                status = 504

        return build_response(content, status)
