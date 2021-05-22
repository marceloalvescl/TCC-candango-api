from models.tipo_turistico import TipoTuristico
from models.ponto_turistico import PontoTuristico
from flask import Blueprint, jsonify, request, current_app
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
                                pais_usuario=request.json["pais_usuario"])
            try:
                db.session.add(usuario)
                db.session.commit()
                return build_response_usuario("Cadastro realizado com sucesso!", usuario), 200 
            except sqlalchemy.exc.IntegrityError as e:
                if(str(e).find('(psycopg2.errors.UniqueViolation)') != -1):
                    return json.loads('"Erro": "O email informado ja existe no banco"'), 409
                logger.log(40, e)
        return build_response("favor enviar json no body", 404)

@candango_routes.route('/api/candango/signin',
                    methods=['POST'])
def candango_singin():
    if request.method == 'POST':
        if request.json: 
            email = request.json['eml_usuario']
            senha = request.json['pwd_usuario']
            usuario = Usuario.query.filter(
                Usuario.eml_usuario.like(email),
                Usuario.pwd_usuario.like(senha)
            ).first()
            if(usuario):
                logger.info("Logando usuário: " + usuario.eml_usuario)
                login_user(usuario)
                response = '{"Sucesso": "Usuário logado"}'
                return json.loads(response), 201
            else:
                response = '{"Erro": "Usuário ou senha inválidos"}'
                return json.loads(response), 401
        else:
            content = "Fornecer usuário e senha!"
            status = 400
            return build_response(content, status)

@candango_routes.route('/api/candango/usuario',
                    methods=['GET'])
@login_required
def candango_usuario():
    if request.method == 'GET':
        if request.json: 
            try:
                email = request.json['eml_usuario']
                usuario = Usuario.query.filter(
                    Usuario.eml_usuario.like(email)
                ).first()
                if(usuario):
                    logger.info("Informações do usuário: " + usuario.eml_usuario)
                    return build_response_usuario("Encontrado", usuario), 201
                else:
                    response = '{"Erro": "Email inexistente"}'
                    return json.loads(response), 401
            except Exception as e :
                logger.error(e)
                content = ""
                status = 504
    
    return build_response(content, status)

@candango_routes.route('/api/candango/pontosTuristicos', methods=['GET'])
@login_required
def candango_lista_pontos_turisticos():
    if request.method == 'GET':
        pontosTuristicos = db.session.query(PontoTuristico).join(Local).all()
        listaJsonPontoTuristico = []
        for pontoTuristico in pontosTuristicos:
            listaJsonPontoTuristico.append(pontoTuristico.toJson())
        print(listaJsonPontoTuristico)
            

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