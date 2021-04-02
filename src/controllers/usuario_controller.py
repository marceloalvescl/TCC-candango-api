from utils.tools import elements_to_dict
from utils.builders import build_response_usuario, build_response
from utils.constants import DB_SCHEMA
from db import queries
from db.database import DataBase
from models.DTO.usuario import Usuario
from models.DAO.usuario_dao import UsuarioDAO
import smtplib
import json



class UsuarioController:

    def __init__(self):
        self.database = DataBase()

    def login(self, content):
        database = DataBase()
        usuario = Usuario(email=content['eml_usuario'], senha=content['pwd_usuario'])
        resultado, usuario = UsuarioDAO().existe(usuario)
        if(resultado):
            return build_response_usuario("Login realizado com sucesso!", usuario), 200
        elif(not resultado):
            return 'Usuário ou senha incorreto', 401
        else: 
            return self.returnResponse(content)

    def signup(self, content):
        self.database = DataBase()
        usuario = Usuario(email=content["eml_usuario"], 
                            senha=content["pwd_usuario"], 
                            nome=content["nme_usuario"], 
                            telefone=content["tlf_usuario"], 
                            genero=content["gen_usuario"],
                            estado=content["est_usuario"],
                            pais=content["pais_usuario"],
                            status=True)
        resultado, usuario = UsuarioDAO().cadastrarNovo(usuario)
        if(resultado):
            return build_response_usuario("Cadastro realizado com sucesso!", usuario), 200
        elif(not resultado):
            return usuario, 409
        else: 
            return self.returnResponse(content)    

    def get_usuario(self, idtUsuario):
        self.database = DataBase()
        sql = queries.SQL_SEL_INFO_USUARIO.format(idtUsuario)
        content = self.database.getOne(sql)
        
        if len(content) == 0:
            return "Usuário ou senha incorreto", 400
        else:
            self.returnResponse(content)

        content = elements_to_dict(usuario_info, queries.SQL_SEL_INFO_USUARIO)
        return content, 200

    def forgot_password(self):
        mail = Mail(self.app_context)

    def returnResponse(self, content):
        if content == "error":
            return "Erro de conexão ao banco", 503
        elif content is None:
            return "No Content", 204

    def post_forgotpass_email(self):
        
        server = smtplib.SMTP('smtp.gmail.com')
        server.ehlo()
        server.starttls()
        server.login("candangoapp@gmail.com","Candango2021")

        msg = "A text!"
        server.sendmail("candangoapp@gmail.com", "marceloalvescl@sempreceub.com", msg)
        server.quit()
        return "Teste", 200