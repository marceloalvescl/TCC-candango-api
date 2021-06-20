from flask import jsonify
from models.usuario import Usuario

def build_response_usuario(msg, resultado):
    if (isinstance(resultado, str)):
        content = {"msg": msg, "problema" : resultado}
    else:
        
        Usuario = resultado
        content = {"msg":msg,
                   "userInfo":{
                            "id": str(Usuario.id_usuario),
                            "email": str(Usuario.eml_usuario), 
                            "name": str(Usuario.nme_usuario), 
                            "phone": str(Usuario.tlf_usuario),
                            "gender": str(Usuario.gen_usuario),
                            "state": str(Usuario.est_usuario),
                            "country": str(Usuario.pais_usuario),
                            "currentAmountExp": str(Usuario.qtd_exp_atual),
                            "level": str(Usuario.cod_level)
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