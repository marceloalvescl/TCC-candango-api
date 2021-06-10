from flask import request
from flask_login import login_required
from routes import candango_routes
from controllers import usuario_controller  
from settings import logger
import json

# Rota /api/candango/user/signup - Método POST
# ["POST"] para cadastrar novo usuário
@candango_routes.route('/api/candango/user/signup', methods=['POST'])
def candango_signup():
    if request.json: 
        return usuario_controller.cadastrarUsuario(request.json)
    return json.loads('{"error" : "Favor enviar JSON na request"}'), 404

# Rota /api/candango/user/signin - Método POST
# ["POST"] para logar usuário cadastrado
@candango_routes.route('/api/candango/user/signin', methods=['POST'])
def candango_singin():
    if request.json: 
        return usuario_controller.logarUsuario(request.json)
    return json.loads('{"error" : "Favor enviar JSON na request"}'), 404

# Rota /api/candango/user/forgotPassword - Métodos POST e PUT
# ["POST"] para receber código de redefinição de senha  
# ["PUT"]  para alterar a senha do usuário
@candango_routes.route('/api/candango/user/forgotPassword', methods=['POST', 'PUT'])
def candango_forgot_password():
    if request.method == 'POST':
        if request.json: 
            return usuario_controller.esqueceuSenha(request.json)
        return json.loads('{"error" : "Favor enviar JSON na request"}'), 404
    elif request.method == 'PUT':
        if request.json: 
            return usuario_controller.alterarSenha(request.json)
        return json.loads('{"error" : "Favor enviar JSON na request"}'), 404        

# Rota /api/candango/user - Métodos POST e PUT
# @login_required - Necessário enviar cookie com sessão válida (autenticação do usuário /api/candango/usuario/signin) 
# ["GET"] para buscar informações do usuário logado
# ["PUT"] para alterar informações do usuário logado
@candango_routes.route('/api/candango/user', methods=['GET', 'PUT'])
@login_required
def candango_user():
    if request.method == 'GET':
        return usuario_controller.informacoesUsuarioLogado()
    elif request.method == 'PUT':
        if request.json:
            return usuario_controller.alterarInfoUsuario(request.json)
        return json.loads('{"error" : "Favor enviar JSON na request"}'), 404
