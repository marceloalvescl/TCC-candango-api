from flask_sqlalchemy import SQLAlchemy
from app import db
from models.medalha import Medalha
from sqlalchemy.types import DateTime
from sqlalchemy  import func

from models.usuario import Usuario

class UsuarioMedalha(db.Model):
    __tablename__ = 'ta_usuario_medalha'
    id_usuario_medalha  = db.Column(db.Sequence('ta_usuario_medalha_id_usuario_medalha_seq'), primary_key=True)
    cod_usuario = db.Column(db.Integer, db.ForeignKey('tb_usuario.id_usuario'))
    cod_medalha = db.Column(db.Integer, db.ForeignKey('tb_medalha.id_medalha'))
    sts_usuario_medalha = db.Column(db.Boolean, nullable=False)
    dta_conquista_medalha = db.Column(db.DateTime, nullable=False)

    def __init__(self, cod_usuario=None, cod_medalha=None, sts_usuario_medalha=True):
        self.cod_usuario = cod_usuario
        self.cod_medalha = cod_medalha
        self.sts_usuario_medalha = sts_usuario_medalha
        self.dta_conquista_medalha = func.current_timestamp()

    def toDict(self):
        medal = Medalha.query.filter(
            Medalha.id_medalha == self.cod_medalha
        ).first()
        userMedal = {
            "userCode" : self.cod_usuario,
            "unlockDate" : self.dta_conquista_medalha,
            "medalha" : medal.toDict()
        }
        return userMedal