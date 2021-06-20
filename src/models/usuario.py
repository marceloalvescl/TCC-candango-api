from app import db, login_manager
from flask_login import UserMixin
from models.level import Level
from sqlalchemy.dialects.postgresql import BYTEA

class Usuario(db.Model, UserMixin):
    __tablename__ = 'tb_usuario'
    id_usuario  = db.Column(db.Integer, db.Sequence('tb_usuario_id_usuario_seq'), primary_key=True)
    cod_level  = db.Column(db.Integer, nullable=False)
    nme_usuario = db.Column(db.String(50), autoincrement=True, primary_key=True)
    eml_usuario = db.Column(db.String(256), nullable=False, unique=True)
    pwd_usuario = db.Column(db.String(256), nullable=False)
    tlf_usuario = db.Column(db.String(22), nullable=False)
    gen_usuario = db.Column(db.String(1), nullable=False)
    est_usuario = db.Column(db.String(100), nullable=False)
    pais_usuario = db.Column(db.String(100), nullable=False)
    status_usuario = db.Column(db.Boolean, nullable=False)
    qtd_exp_atual= db.Column(db.Integer, nullable=False)
    bytea_fto_conta = db.Column(BYTEA, nullable=True)
    cod_recuperar_senha = db.Column(db.String(6), nullable=True)

    medalhas = db.relationship('Medalha', secondary='ta_usuario_medalha', backref=db.backref('medalhas_usuario', lazy='dynamic'))
    attractions = db.relationship('PontoTuristico', secondary='ta_usuario_ponto_turistico', backref=db.backref('pontos_turisticos_usuario', uselist=False))
    
    def __init__(self, cod_level=1, nme_usuario=None, eml_usuario=None, pwd_usuario=None, 
                tlf_usuario=None, gen_usuario=None, est_usuario=None, pais_usuario=None, 
                status_usuario=True, qtd_exp_atual=0, bytea_fto_conta=None, cod_recuperar_senha=None):
        self.cod_level      = cod_level
        self.nme_usuario    = nme_usuario
        self.eml_usuario    = eml_usuario
        self.pwd_usuario    = pwd_usuario
        self.tlf_usuario    = tlf_usuario
        self.gen_usuario    = gen_usuario
        self.est_usuario    = est_usuario
        self.pais_usuario   = pais_usuario
        self.status_usuario = status_usuario
        self.qtd_exp_atual  = qtd_exp_atual
        self.bytea_fto_conta  = bytea_fto_conta
        self.cod_recuperar_senha = cod_recuperar_senha
    
    def addExp(self, incomingExp):
        levelAtual = Level.query.filter(
            Level.id_level == self.cod_level
        ).first()

        if(levelAtual.qtd_experiencia < (incomingExp + self.qtd_exp_atual)):
            print("subindo de nível")
            self.cod_level += 1
            self.qtd_exp_atual = 0
        else:
            self.qtd_exp_atual += incomingExp

    def toDict(self):
        usuario = {
            "name": self.nme_usuario,
            "email":self.eml_usuario, 
            "phone": self.tlf_usuario, 
            "gender": self.gen_usuario,
            "country" : self.pais_usuario,
            "state": self.est_usuario,
            "status" : self.status_usuario,
            "level": self.cod_level, 
            "exp" : self.qtd_exp_atual,
            "photo" : ""
        }
        return usuario

    def get_id(self):
        print(self.id_usuario)
        return(self.id_usuario)
    
    def __str__(self):
        usuario = '''id={0}: [level={1}, nome={2}, email={3}, senha={4}, telefone={5}, 
                        genero={6}, estado={7}, pais={7}, status={8}, qtdExp={9}, urlFoto={10}]'''.format(
                                                    self.id_usuario, self.cod_level, self.nme_usuario, 
                                                    self.eml_usuario, self.pwd_usuario, self.tlf_usuario,
                                                    self.gen_usuario, self.est_usuario, self.pais_usuario,
                                                    self.status_usuario, self.qtd_exp_atual, self.bytea_fto_conta)
        return usuario                                                                                        
    

#standalone callback function
@login_manager.user_loader
def get_user(idUsuario):
    return Usuario.query.filter_by(id_usuario=idUsuario).first()