from flask import jsonify
from models.usuario import Usuario
from controllers import level_controller

def build_response_usuario(msg, resultado):
    if (isinstance(resultado, str)):
        content = {"msg": msg, "problema" : resultado}
    else:
        
        usuario = resultado
        content = {"msg":msg,
                   "userInfo":{
                            "id": str(usuario.id_usuario),
                            "email": str(usuario.eml_usuario), 
                            "name": str(usuario.nme_usuario), 
                            "phone": str(usuario.tlf_usuario),
                            "gender": str(usuario.gen_usuario),
                            "state": str(usuario.est_usuario),
                            "country": str(usuario.pais_usuario),
                            "currentAmountExp": str(usuario.qtd_exp_atual),
                            "level": str(usuario.cod_level),
                            "currentLevel" : level_controller.getLevelById(usuario.cod_level) 
                        }
                    }
    return content

def build_response(content, status):
    print(content)
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
    
    content = {
            'msg': msg,
            'user': user.toDict(),
            'attractions' : attractions
        }

    return content, status

def email_message_template(usuario):
    msg = f'''Subject: Código de redefinição de senha! \n\n
                Olá {usuario.nme_usuario}, \n\n
                    Seu código para redefinir a senha é: {str(usuario.cod_recuperar_senha)}\n\n 
                Atenciosamente, CandanGO!'''.encode('utf-8')
    return msg