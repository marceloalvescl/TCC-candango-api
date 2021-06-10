from models.tipo_turistico import TipoTuristico
from models.ponto_turistico import PontoTuristico
from flask_login import login_user, logout_user, current_user, login_required
from flask import send_file
from settings import logger
import json
from models.ponto_turistico import PontoTuristico
from routes import candango_routes
from controllers import medalha_controller

# Rota /api/candango/medals/user - Métodos GET
# @login_required - Necessário enviar cookie com sessão válida (autenticação do usuário /api/candango/usuario/signin) 
# ["GET"] para buscar medalhas liberadas pelo usuário logado
@candango_routes.route('/api/candango/medals/user', methods=['GET'])
@login_required
def candango_medalhas_usuario():
    content, status = medalha_controller.medalhas_usuario()
    return content, status

# Rota /api/candango/medals/user - Métodos GET
# @login_required - Necessário enviar cookie com sessão válida (autenticação do usuário /api/candango/usuario/signin) 
# ["GET"] para buscar todas as medalhas
@candango_routes.route('/api/candango/medals', methods=['GET'])
@login_required
def candango_medalhas():
    content, status = medalha_controller.todas_medalhas()
    return content, status

# Rota /api/candango/medals/image/<image> - Métodos GET
# ["GET"] para buscar a imagem da medalha passada como parâmetro
@candango_routes.route('/api/candango/medals/image/<image>', methods=['GET'])
def candango_imagem(image):
    try:
        logger.info(image)
        return send_file('D:\\TCC-candango-api\\src\\utils\\imagens\\{0}.jpg'.format(image), mimetype='image/jpg'), 200
    except Exception as e:
        logger.fatal(e)
        content = '{"error" : "imagem inexistente!"}'
        status = 404
        return json.loads(content), status