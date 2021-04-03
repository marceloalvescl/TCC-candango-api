


class Usuario:

    def __init__(self, idUsuario=None, email=None, senha=None, nome=None, telefone=None, 
                        genero=None, estado=None, pais=None, status=None, quantidadeExpAtual=None, 
                            urlFotoConta=None, codLevel=None, codRecuperarSenha=None ):
        self.idUsuario = idUsuario
        self.codLevel = codLevel
        self.nome = nome
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.genero = genero
        self.estado = estado
        self.pais = pais
        self.status = status
        self.quantidadeExpAtual = quantidadeExpAtual
        self.urlFotoConta = urlFotoConta 
        self.codRecuperarSenha = codRecuperarSenha
    
    def getIdUsuario(self):
        return self.idUsuario

    def setIdUsuario(self, idUsuario):
        self.idUsuario = idUsuario

    def getEmail(self):
        return self.email
    
    def setEmail(self, email):
        self.email = email
    
    def getSenha(self):
        return self.senha
    
    def setSenha(self, senha):
        self.senha = senha

    def getNome(self):
        return self.nome
    
    def setNome(self, nome):
        self.nome = nome
    
    def getGenero(self):
        return self.genero
    
    def setGenero(self, genero):
        self.genero = genero

    def getEstado(self):
        return self.estado
    
    def setEstado(self, estado):
        self.estado = estado

    def getTelefone(self):
        return self.telefone
    
    def setTelefone(self, telefone):
        self.telefone = telefone
    
    def getPais(self):
        return self.pais

    def setPais(self, pais):
        self.pais = pais

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status

    def getQuantidadeExpAtual(self):
        return self.quantidadeExpAtual

    def setQuantidadeExpAtual(self, quantidadeExpAtual):
        self.quantidadeExpAtual = quantidadeExpAtual
    
    def getCodLevel(self):
        return self.codLevel
    
    def setCodLevel(self, codLevel):
        self.codLevel = codLevel

    def getUrlFtoConta(self):
        return self.getUrlFtoConta

    def setUrlFotoConta(self, urlFotoConta):
        self.urlFotoConta = urlFotoConta
    
    def getUrlFotoConta(self):
        return self.urlFotoConta

    def setCodRecuperarSenha(self, codRecuperarSenha):
        self.codRecuperarSenha = codRecuperarSenha

    def getCodRecuperarSenha(self):
        return self.codRecuperarSenha