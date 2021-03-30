from utils.tools import elements_to_dict
from utils.builders import build_response_usuario, build_response_login
from utils.contants import DB_SCHEMA
from db import queries
from db.database import DataBase
from models.usuario import Usuario
import json

class UsuarioController:

    def __init__(self):
        self.database = DataBase()

    def login(self, content):
        database = DataBase()
        sql = queries.SQL_SEL_LOGIN_USUARIO.format(content["eml_usuario"], content["pwd_usuario"])
        content = self.database.getOne(sql)

        if len(content) == 0:
            return 'Usuário ou senha incorreto', 400
        else:
            self.returnResponse(content)

        usuario_info = elements_to_dict(content, queries.SQL_SEL_LOGIN_USUARIO)
        usuarioObj = Usuario(usuario_info[0], usuario_info[1], usuario_info[2], usuario_info[3], None, None, usuario_info[4], usuario_info[5])
        content = build_response_login("Login realizado com sucesso!", usuarioObj)
        return content, 200

    def signup(self, content):
        self.database = DataBase()
        usuarioObj = Usuario(None, content["eml_usuario"], content["pwd_usuario"], content["nme_usuario"], None, None, None, None)
        sql = queries.SQL_INS_USU_CANDANGO.format(usuarioObj.getNome(), usuarioObj.getEmail(), usuarioObj.getSenha())
        content = self.database.insert_new_element(sql)
        content = [str(content)]
        content.append(1)
        if(self.returnResponse(content) is not None):
            return self.returnResponse(content) 
        content = "Cadastro realizado com sucesso!"
        return content, 200

    def get_usuario(self, idtUsuario):
        self.database = DataBase()
        sql = queries.SQL_SEL_INFO_USUARIO.format(idtUsuario)
        content = self.database.getOne(sql)
        
        if len(content) == 0:
            return 'Usuário ou senha incorreto', 400
        else:
            self.returnResponse(content)

        content = elements_to_dict(usuario_info, queries.SQL_SEL_INFO_USUARIO)
        return content, 200

    def returnResponse(self, content):
        if content == 'error':
            return 'Erro de conexão ao banco', 503
        elif content is None:
            return 'No Content', 204
