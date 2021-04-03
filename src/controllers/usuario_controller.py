from utils.tools import elements_to_dict
from utils.builders import build_response_usuario, build_response
from utils.constants import DB_SCHEMA
from db import queries
from db.database import DataBase
from models.DTO.usuario import Usuario
from models.DAO.usuario_dao import UsuarioDAO
from smtplib import SMTP
import json



class UsuarioController:

    def __init__(self):
        self.database = DataBase()

    def login(self, content):
        database = DataBase()
        resultado, usuario = UsuarioDAO().buscarPorEmailESenha(email=content['eml_usuario'], senha=content['pwd_usuario'])
        if(resultado):
            return build_response_usuario("Login realizado com sucesso!", usuario), 200
        else:
            return 'Usuário ou senha incorreto', 401

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
        else:
            return usuario, 409

    def forgot_password(self, content):
        with SMTP('smtp.gmail.com') as smtp:
            resultado, usuario = UsuarioDAO().gerarCodigoRecuperarSenha(content['eml_usuario'])
            smtp.ehlo()
            smtp.starttls()
            smtp.login("candangoapp@gmail.com","Candango2021")
            msg = usuario.getCodRecuperarSenha()
            smtp.sendmail("candangoapp@gmail.com", content['eml_usuario'], msg)
            smtp.quit()
            return "Email com código de redefinição enviado!", 200
    
    def change_password(self, content):
        resultado, msg = UsuarioDAO().alterarSenhaUsuario(content['eml_usuario'], content['cod_recuperar_senha'], content['nova_senha'])
        if(resultado):
            return msg, 200
        elif(not resultado):
            return usuario, 401
