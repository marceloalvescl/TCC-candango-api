from routes import candango_routes
from controllers import usuario_controller  
from settings.settings import logger

from flask import request
from flask_login import login_required

# Rota /api/candango/user/signup - Método POST
# ["POST"] para cadastrar novo usuário
@candango_routes.route('/user/signup', methods=['POST'])
def candango_signup():
    if request.json:
        return usuario_controller.cadastrarUsuario(request.json)
    return {"error" : "Favor enviar JSON na request"}, 404

# Rota /api/candango/user/signin - Método POST
# ["POST"] para logar usuário cadastrado
@candango_routes.route('/user/signin', methods=['POST'])
def candango_singin():
    if request.json:
        return usuario_controller.logarUsuario(request.json)
    return {"error" : "Favor enviar JSON na request"}, 404

# Rota /api/candango/user/signout - Método GET
# @login_required - Necessário enviar cookie com sessão válida (autenticação do usuário /api/candango/usuario/signin) 
# ["GET"] para deslogar usuário cadastrado
@candango_routes.route('/user/signout', methods=['GET'])
#@login_required
def candango_signout():
    return usuario_controller.deslogarUsuario()

# Rota /api/candango/user/forgotPassword - Métodos POST e PUT
# ["POST"] para receber código de redefinição de senha  
# ["PUT"]  para alterar a senha do usuário
@candango_routes.route('/user/forgotPassword', methods=['POST', 'PUT'])
def candango_forgot_password():
    if request.method == 'POST':
        if request.json: 
            return usuario_controller.esqueceuSenha(request.json)
        return {"error" : "Favor enviar JSON na request"}, 404
    elif request.method == 'PUT':
        if request.json: 
            logger.info(request.json)
            return usuario_controller.alterarSenha(request.json)
        return {"error" : "Favor enviar JSON na request"}, 404        

# Rota /api/candango/user - Métodos POST e PUT
# @login_required - Necessário enviar cookie com sessão válida (autenticação do usuário /api/candango/usuario/signin) 
# ["GET"] para buscar informações do usuário logado
# ["PUT"] para alterar informações do usuário logado
@candango_routes.route('/user', methods=['GET', 'PUT'])
@login_required
def candango_user():
    if request.method == 'GET':
        return usuario_controller.informacoesUsuarioLogado()
    elif request.method == 'PUT':
        if request.json:
            if 'oldPassword' in request.json and 'newPassword' in request.json:
                return usuario_controller.alterarSenhaUsuarioLogado(request.json)
            else:
                return usuario_controller.alterarInfoUsuario(request.json)
        return {"error" : "Favor enviar JSON na request"}, 404

# Rota /api/candango/user/deactivate - Métodos GET
# @login_required - Necessário enviar cookie com sessão válida (autenticação do usuário /api/candango/usuario/signin) 
# ["GET"] para desativar conta do usuário logado
@candango_routes.route('/user/deactivate', methods=['GET'])
@login_required
def candango_user_deactivate():
    if request.method == 'GET':
        return usuario_controller.desativarContaUsuario()
    

# Rota /api/candango/user - Métodos POST e PUT
# @login_required - Necessário enviar cookie com sessão válida (autenticação do usuário /api/candango/usuario/signin) 
# ["GET"] para buscar imagem do perfil do usuário logado
# ["PUT"] para enviar ou alterar imagem do perfil do usuário logado
@candango_routes.route('/user/image', methods=['POST', 'GET'])
@login_required
def candango_user_image():
    if request.method == 'POST':
        return usuario_controller.setImagemPerfil(request.files['image'])
    if request.method == 'GET':
        return usuario_controller.getImagemPerfil()
    