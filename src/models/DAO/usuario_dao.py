from db.database import DataBase
from models.DTO.usuario import Usuario
from db import queries 



class UsuarioDAO():

    def buscarPorEmailESenha(self, email, senha):
        database = DataBase()
        sql = queries.SQL_SEL_LOGIN_USUARIO.format(email, senha)
        resultado = database.getOne(sql)
        if(resultado is not None):
            usuario = self.instanciaUsuarioAPartirDaConsulta(resultado)
            return True, usuario
        else:
            return False, usuario

    def buscarPorId(self, idtUsuario):
        database = Database()
        sql = queries.SQL_SEL_USUARIO_POR_ID(idtUsuario)
        resultado = database.getOne(sql)
        if(resultado is not None):
            usuario = instanciaUsuarioAPartirDaConsulta(resultado)
            return True, usuario
        else:
            return False
    
    def cadastrarNovo(self, usuario):
        self.database = DataBase()
        sql = queries.SQL_INS_USU_CANDANGO.format(usuario.getNome(), usuario.getEmail(), 
                                                usuario.getSenha(), usuario.getTelefone(), 
                                                usuario.getGenero(), usuario.getEstado(), 
                                                usuario.getPais(), usuario.getStatus())
        resultado = self.database.insert_new_element(sql)
        if(resultado is not None):
            resultado, usuario = self.buscarPorEmailESenha(usuario.getEmail(), usuario.getSenha())   
            return resultado, usuario
        else:
            return False, "Email já cadastrado!"
        
    def instanciaUsuarioAPartirDaConsulta(self, resultadoConsulta):
        return Usuario(idUsuario=resultadoConsulta[0], codLevel=resultadoConsulta[1], nome=resultadoConsulta[2], email=resultadoConsulta[4], 
                            telefone=resultadoConsulta[5], genero=resultadoConsulta[6], estado=resultadoConsulta[7], pais=resultadoConsulta[8], 
                            status=resultadoConsulta[9], quantidadeExpAtual=resultadoConsulta[10], urlFotoConta=resultadoConsulta[11])