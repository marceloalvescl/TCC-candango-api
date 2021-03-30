from db.database import DataBase
from models.DTO.usuario import Usuario
from db import queries 



class UsuarioDAO():

    def existe(self, usuario):
        self.database = DataBase()
        sql = queries.SQL_SEL_LOGIN_USUARIO.format(usuario.getEmail(), usuario.getSenha())
        resultado = self.database.getOne(sql)
        if(resultado is not None):
            usuario = Usuario(idUsuario=resultado[0], email=resultado[1], senha=resultado[2], 
                        nome=resultado[3], quantidadeExpAtual=resultado[4], codLevel=resultado[5])
            return True, usuario
        else:
            return False, usuario
        
    def cadastrarNovo(self, usuario):
        self.database = DataBase()
        sql = queries.SQL_INS_USU_CANDANGO.format(usuario.getNome(), usuario.getEmail(), usuario.getSenha())
        resultado = self.database.insert_new_element(sql)
        if(resultado is not None):
            resultado, usuario = self.existe(usuario)   
            return resultado, usuario
        else:
            return False