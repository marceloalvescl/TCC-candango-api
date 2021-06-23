from routes import candango_routes
from controllers import medalha_controller

from flask_login import login_required
from flask import request
import json

# Rota /api/candango/medals/user - Métodos GET
# @login_required - Necessário enviar cookie com sessão válida (autenticação do usuário /api/candango/usuario/signin) 
# ["GET"] para buscar medalhas liberadas pelo usuário logado
# ["PUT"] para cadastrar medalha para usuário
@candango_routes.route('/medals/user', methods=['GET', 'POST'])
@login_required
def candango_medalhas_usuario():
    if request.method == "GET":
        return medalha_controller.getUserMedal()
    if request.method == "POST":
        if request.json:
            return medalha_controller.setUserMedal(request.json)
        else:
            return {"error" : "Favor enviar JSON na request"}, 404             
        
        

# Rota /api/candango/medals/user - Métodos GET
# @login_required - Necessário enviar cookie com sessão válida (autenticação do usuário /api/candango/usuario/signin) 
# ["GET"] para buscar todas as medalhas
@candango_routes.route('/medals', methods=['GET'])
@login_required
def candango_medalhas():
    return medalha_controller.getMedalhas()

# Rota /api/candango/medals/image/<image> - Métodos GET
# ["GET"] para buscar a imagem da medalha passada como parâmetro
@candango_routes.route('/medals/image/<image>', methods=['GET'])
def candango_imagem(image):
    return medalha_controller.getMedalhaImagem(image)