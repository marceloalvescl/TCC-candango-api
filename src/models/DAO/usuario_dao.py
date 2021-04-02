from db.database import DataBase
from models.DTO.usuario import Usuario
from db import queries 



class UsuarioDAO():

    def existe(self, usuario):
        database = DataBase()
        sql = queries.SQL_SEL_LOGIN_USUARIO.format(usuario.getEmail(), usuario.getSenha())
        resultado = database.getOne(sql)
        print(sql)
        print(resultado)
        if(resultado is not None):
            usuario = Usuario(idUsuario=resultado[0], codLevel=resultado[1], nome=resultado[2], email=resultado[3], senha=resultado[4], telefone=resultado[5], genero=resultado[6],
                                    estado=resultado[7], pais=resultado[8], status=resultado[9], quantidadeExpAtual=resultado[10], urlFotoConta=resultado[11])
            
            return True, usuario
        else:
            return False, usuario
        
    def cadastrarNovo(self, usuario):
        self.database = DataBase()
        sql = queries.SQL_INS_USU_CANDANGO.format(usuario.getNome(), usuario.getEmail(), 
                                                usuario.getSenha(), usuario.getTelefone(), 
                                                usuario.getGenero(), usuario.getEstado(), 
                                                usuario.getPais(), usuario.getStatus())
        resultado = self.database.insert_new_element(sql)
        if(resultado is not None):
            resultado, usuario = self.existe(usuario)   
            return resultado, usuario
        else:
            return False, "Email já cadastrado!"
        