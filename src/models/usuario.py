from app import db, login_manager
from flask_login import UserMixin


UsuarioMedalha = db.Table('usuario_medalha',
    db.Column('cod_usuario', db.Integer, db.ForeignKey('tb_usuario.id_usuario')),
    db.Column('cod_medalha', db.Integer, db.ForeignKey('tb_medalha.id_medalha'))
)

class Medalha(db.Model):
    __tablename__ = 'tb_medalha'
    id_medalha  = db.Column(db.Integer, db.Sequence('tb_medalha_id_medalha_seq'), primary_key=True)
    nme_medalha = db.Column(db.String(75), nullable=False)
    url_img_medalha = db.Column(db.Text, nullable=True)
    qtd_experiencia = db.Column(db.Integer, nullable=True)
    


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
    url_fto_conta = db.Column(db.Text, nullable=True)

    medalhas = db.relationship('Medalha', secondary='usuario_medalha', backref=db.backref('medalhas_usuario', lazy='dynamic'))
    
    def __init__(self, cod_level=1, nme_usuario=None, eml_usuario=None, pwd_usuario=None, 
                    tlf_usuario=None, gen_usuario=None, est_usuario=None, pais_usuario=None, status_usuario=True, qtd_exp_atual=0, url_fto_conta=None):
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
        self.url_fto_conta  = url_fto_conta
    
    def get_id(self):
        print(self.id_usuario)
        return(self.id_usuario)
    
    def __str__(self):
        usuario = '''id={0}: [level={1}, nome={2}, email={3}, senha={4}, telefone={5}, 
                        genero={6}, estado={7}, pais={7}, status={8}, qtdExp={9}, urlFoto={10}]'''.format(
                                                    self.id_usuario, self.cod_level, self.nme_usuario, 
                                                    self.eml_usuario, self.pwd_usuario, self.tlf_usuario,
                                                    self.gen_usuario, self.est_usuario, self.pais_usuario,
                                                    self.status_usuario, self.qtd_exp_atual, self.url_fto_conta)
        return usuario                                                                                        
    

#standalone callback function
@login_manager.user_loader
def get_user(idUsuario):
    return Usuario.query.filter_by(id_usuario=idUsuario).first()