from flask import jsonify

def build_response_usuario(msg, resultado):
    if (isinstance(resultado, str)):
        content = {"msg": msg, "problema" : resultado}
    else:
        Usuario = resultado
        content = {"msg":msg,
                   "usuarioInfo":{
                            "idUsuario": str(Usuario.getIdUsuario()),
                            "emailUsuario": str(Usuario.getEmail()), 
                            "nomeUsuario": str(Usuario.getNome()), 
                            "quantidadeExpAtual": str(Usuario.getQuantidadeExpAtual()),
                            "codLevel": str(Usuario.getCodLevel())
                        }
                    }
    return content

def build_response(content, status):
    if isinstance(content, dict) or isinstance(content, list):

        if status == 201:
            content['msg'] = f'Criado item com id {content} com sucesso'
        
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

    return jsonify(content), status

