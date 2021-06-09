from flask import request
from flask_login import login_required
from routes import candango_routes
from controllers import usuario_controller  
from settings import logger
import json

# Rota para cadastrar novo usuário
@candango_routes.route('/api/candango/signup', methods=['POST'])
def candango_signup():
    if request.json: 
        return usuario_controller.cadastrarUsuario(request.json)
    return json.loads('{"error" : "Favor enviar JSON na request"}'), 404

# Rota para logar usuário cadastrado
@candango_routes.route('/api/candango/signin', methods=['POST'])
def candango_singin():
    if request.json: 
        return usuario_controller.logarUsuario(request.json)
    return json.loads('{"error" : "Favor enviar JSON na request"}'), 404

# Rota para enviar código de redefinição de senha
@candango_routes.route('/api/candango/forgotPassword', methods=['POST'])
def candango_forgot_password():
    if request.json: 
        return usuario_controller.esqueceuSenha(request.json)
    return json.loads('{"error" : "Favor enviar JSON na request"}'), 404

# Rota para alterar a senha do usuário
@candango_routes.route('/api/candango/changePassword', methods=['POST'])
def candango_change_password():
    if request.json: 
        return usuario_controller.alterarSenha(request.json)
    return json.loads('{"error" : "Favor enviar JSON na request"}'), 404

# Rota para buscar informações do usuário logado
@candango_routes.route('/api/candango/usuario', methods=['GET'])
@login_required
def candango_usuario():
    return usuario_controller.informacoesUsuarioLogado()

# Rota para alterar informações do usuário
@candango_routes.route('/api/candango/alterarUsuario', methods=['POST'])
@login_required
def candango_update_user():
    if request.json:
        return usuario_controller.alterarInfoUsuario(request.json)
    return json.loads('{"error" : "Favor enviar JSON na request"}'), 404