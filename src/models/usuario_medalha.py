from app import db
from models.medalha import Medalha
from sqlalchemy  import func
import datetime
from settings import logger



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
        lastVisit = self.dta_conquista_medalha.strftime('%d-%m-%Y')
        logger.info(lastVisit)
        userMedal = {
            "userCode" : self.cod_usuario,
            "unlockDate" : lastVisit,
            "unlockDate1" : self.dta_conquista_medalha,
            "medalha" : medal.toDict()
        }
        return userMedal