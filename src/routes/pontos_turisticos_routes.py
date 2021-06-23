from routes import candango_routes
from controllers import attraction_controller

from flask import request
from flask_login import login_required
import json

# Rota /api/candango/attractions - Métodos GET
# @login_required - Necessário enviar cookie com sessão válida (autenticação do usuário /api/candango/user/signin) 
# ["GET"] para buscar informações de todos os pontos turísticos
@candango_routes.route('/attractions', methods=['GET'])
@login_required
def candango_lista_pontos_turisticos():
    if request.method == 'GET':
        return {'attractions': attraction_controller.getAllAttractions()}

# Rota /api/candango/attractions/user - Métodos GET
# @login_required - Necessário enviar cookie com sessão válida (autenticação do usuário /api/candango/user/signin) 
# ["GET"] para buscar informações de todos os pontos turísticos visitados pelo usuário <attraction_controller.getAllUserVisitedAttractions>
# ["POST"] para adicionar visita ou incrementar visitas do usuário ao ponto turístico <attraction_controller.setUserVisitedAttraction>
@candango_routes.route('/attractions/user', methods=['GET', 'POST'])
@login_required
def candango_visited_attractions():
    if request.method == 'GET':
        return attraction_controller.getAllUserVisitedAttractions()
    if request.method == 'POST':
        if request.json:
            return attraction_controller.setUserVisitedAttraction(request.json)
        else:
            return '{"error" : "Favor enviar JSON na request"}', 404             

# Rota /api/candango/user/image - Métodos POST e GET
# @login_required - Necessário enviar cookie com sessão válida (autenticação do usuário /api/candango/usuario/signin) 
# ["POST"] para enviar ou alterar imagem do ponto turístico encontrado pelo id 
# ["GET"] para buscar imagem do ponto turistico encontrado pelo id
@candango_routes.route('/attraction/image/<id>', methods=['POST', 'GET'])
def candango_attraction_image(id):
    if request.method == 'POST':
        return attraction_controller.setImagemAttraction(request.files['image'], id)
    if request.method == 'GET':
        return attraction_controller.getImagemAttraction(id)