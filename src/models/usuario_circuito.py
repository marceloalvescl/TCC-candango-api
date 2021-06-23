from app import db
from models.circuito import Circuito
from sqlalchemy  import func
import datetime
from settings import logger



class UsuarioCircuito(db.Model):
    __tablename__ = 'ta_usuario_circuito'
    id_usuario_circuito  = db.Column(db.Sequence('ta_usuario_medalha_id_usuario_medalha_seq'), primary_key=True)
    cod_usuario = db.Column(db.Integer, db.ForeignKey('tb_usuario.id_usuario'))
    cod_circuito = db.Column(db.Integer, db.ForeignKey('tb_circuito.id_circuito'))
    dta_conquista_circuito = db.Column(db.DateTime, nullable=False)

    def __init__(self, cod_usuario=None, cod_circuito=None):
        self.cod_usuario = cod_usuario
        self.cod_circuito = cod_circuito
        self.dta_conquista_circuito = func.current_timestamp()

    def toDict(self):
        circuito = Circuito.query.filter(
            Circuito.id_circuito == self.cod_circuito
        ).first()
        current_time = datetime.datetime.now()
        difference =  current_time - self.dta_conquista_circuito
        logger.info("Circuito desbloqueado há " + str(difference.days) + " dias")
        userCircuit = {
            "userCode" : self.cod_usuario,
            "unlockDate" : self.dta_conquista_circuito,
            "medalha" : circuito.toDict()
        }

        return userCircuit