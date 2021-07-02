from flask import jsonify
from models.usuario import Usuario
from controllers import level_controller, attraction_controller
from settings.settings import logger

def build_response_usuario(msg, resultado):
    if (isinstance(resultado, str)):
        content = {"msg": msg, "problema" : resultado}
    else:
        
        usuario = resultado
        content = {"msg":msg,
                   "userInfo":usuario.toDict()
                    }
    return content

def build_response(content, status):
    if isinstance(content, dict) or isinstance(content, list):

        if status == 201:
            content['msg'] = f'Criado item com id {content} com sucesso'
            
        content['status'] = status
        return jsonify(content), status

    elif isinstance(content, str):
        if status == 201:
            content = {'msg': f'Criado item com id {content} com sucesso'}

        elif status >= 400:
            content = {'msg': content}
            
        else:
            content = {'msg': content}
    else:
        content = {'msg': 'Internal server error!'}

    content['status'] = status
    return jsonify(content), status

def build_response_login(msg, user, attractions, status):
    try:
        userVisitedAttractions, _ = attraction_controller.getAllUserVisitedAttractions()
    except AttributeError as e:
        userVisitedAttractions = {'attractions' : []}
    content = {
            'msg': msg,
            'user': user.toDict(),
            'attractions' : attractions['attractions'],
            'userVisitedAttractions' : userVisitedAttractions['attractions']
        }

    return content, status

def email_message_template(usuario):
    msg = f'''Subject: Código de redefinição de senha CandanGO! \n\n
Olá {usuario.nme_usuario}, \n\n
    Seu código para redefinir a senha é: {str(usuario.cod_recuperar_senha)}\n\n 
Atenciosamente, CandanGO!'''.encode('utf-8')
    return msg