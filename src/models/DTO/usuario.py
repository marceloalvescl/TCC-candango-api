


class Usuario:

    def __init__(self, idUsuario=None, email=None, senha=None, nome=None, telefone=None, sexo=None, quantidadeExpAtual=None, codLevel=None ):
        self.idUsuario = idUsuario
        self.email = email
        self.senha = senha
        self.nome = nome
        self.telefone = telefone
        self.sexo = sexo
        self.quantidadeExpAtual = quantidadeExpAtual
        self.codLevel = codLevel
    
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

    def getTelefone(self):
        return self.telefone

    def setTelefone(self, telefone):
        self.telefone = telefone

    def getSexo(self):
        return self.sexo 

    def setSexo(self, sexo):
        self.sexo = sexo 

    def getQuantidadeExpAtual(self):
        return self.quantidadeExpAtual

    def setQuantidadeExpAtual(self, quantidadeExpAtual):
        self.quantidadeExpAtual = quantidadeExpAtual
    
    def getCodLevel(self):
        return self.codLevel
    
    def setCodLevel(self, codLevel):
        self.codLevel = codLevel
    