from flask import Blueprint, jsonify, request, current_app
from flask_cors import CORS
from utils.builders import build_response_usuario, build_response
from settings import logger
from models.usuario import Usuario
import sqlalchemy 
from app import db

candango_routes = Blueprint('candango', __name__)
CORS(candango_routes)

@candango_routes.route('/api/candango/signup',
                    methods=['POST'])
def candango_signup():
    if request.method == 'POST':
        if request.json: 
            usuario = Usuario(
                                eml_usuario=request.json["eml_usuario"], 
                                pwd_usuario=request.json["pwd_usuario"], 
                                nme_usuario=request.json["nme_usuario"],
                                tlf_usuario=request.json["tlf_usuario"],
                                gen_usuario=request.json["gen_usuario"],
                                est_usuario=request.json["est_usuario"],
                                pais_usuario=request.json["pais_usuario"],
                                )
                                
            '''usuario = Usuario(
                            eml_usuario='testandoestafuncionalidade@gmail.com',
                            pwd_usuario='121213431',
                            nme_usuario='Vitin da Tasmania',
                            tlf_usuario='6199870-2660',
                            gen_usuario='M',
                            est_usuario='DF',
                            pais_usuario='Brasil')'''
                            
            try:
                db.session.add(usuario)
                resultado =db.session.commit()
                print(usuario)
                print(type(usuario))
                print("88*************************88")
                print(resultado)   
                return build_response_usuario("Cadastro realizado com sucesso!", usuario), 200 
            except sqlalchemy.exc.IntegrityError as e:
                print(e)        
        else:
            
            print(request.json)
            username = request.json['eml_usuario']
            password = request.json['pwd_usuario']
            print(username)
            user = Usuario.query.filter(
                            Usuario.email.like(username),
                            Usuario.senha.like(password)).first()
            status = 409
            content = user
            return user, 409
    return build_response("content", 401)

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
            content, status = UsuarioController().buscar_usuario_por_email(request.json)
        except Exception as e :
            print(e)
            content = ""
            status = 504
    
    return build_response(content, status)

@candango_routes.route('/api/candango/forgotPassword', methods=['POST'])
def candango_forgot_password():
    if request.method == 'POST':
        try:
            print("wtf")
            content, status = UsuarioController().forgot_password(request.json)
        except Exception as e :
            logger.fatal(e)
            content = ""
            status = 504

    return build_response(content, status)

@candango_routes.route('/api/candango/changePassword', methods=['POST'])
def candango_change_password():
    if request.method == 'POST':
        try:
            content, status = UsuarioController().change_password(request.json)
        except Exception as e :
            logger.fatal(e)
            content = ""
            status = 504

    return build_response(content, status)

@candango_routes.route('/api/candango/alterarUsuario', methods=['POST'])
def candango_update_user():
    if request.method == 'POST':
        try:
            content, status = UsuarioController().alterarUsuario(request.json)
        except Exception as e :
            logger.fatal(e)
            content = ""
            status = 504

    return build_response(content, status)