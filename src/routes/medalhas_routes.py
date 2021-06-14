from models.tipo_turistico import TipoTuristico
from models.ponto_turistico import PontoTuristico
from flask_login import login_user, logout_user, current_user, login_required
from flask import send_file, request
from settings import logger
import json
from models.ponto_turistico import PontoTuristico
from routes import candango_routes
from controllers import medalha_controller

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
            return json.loads('{"error" : "Favor enviar JSON na request"}'), 404             
        
        

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
    try:
        logger.info(image)
        return send_file('D:\\TCC-candango-api\\src\\utils\\imagens\\{0}.jpg'.format(image), mimetype='image/jpg'), 200
    except Exception as e:
        logger.fatal(e)
        content = '{"error" : "imagem inexistente!"}'
        status = 404
        return json.loads(content), status