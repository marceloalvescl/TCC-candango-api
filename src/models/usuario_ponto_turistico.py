from app import db
from models.ponto_turistico import PontoTuristico
from sqlalchemy  import func



class UsuarioPontoTuristico(db.Model):
    __tablename__ = 'ta_usuario_ponto_turistico'
    id_usuario_ponto_turistico  = db.Column(db.Sequence('ta_usuario_ponto_turistico_id_usuario_ponto_turistico_seq'), primary_key=True)
    cod_usuario = db.Column(db.Integer, db.ForeignKey('tb_usuario.id_usuario'))
    cod_ponto_turistico = db.Column(db.Integer, db.ForeignKey('tb_ponto_turistico.id_ponto_turistico'))
    qtd_visitas = db.Column(db.Integer, nullable=False)
    url_img_usuario_ponto_turistico = db.Column(db.Text, nullable=True)
    dta_usuario_ponto_turistico = db.Column(db.DateTime, nullable=False)

    def __init__(self, cod_usuario=None, cod_ponto_turistico=None, qtd_visitas=None, url_img_usuario_ponto_turistico=None):
        self.cod_usuario = cod_usuario
        self.cod_ponto_turistico = cod_ponto_turistico
        self.qtd_visitas = qtd_visitas
        self.url_img_usuario_ponto_turistico = url_img_usuario_ponto_turistico
        self.dta_usuario_ponto_turistico = func.current_timestamp()

    def toDict(self):
        attraction = PontoTuristico.query.filter(
            PontoTuristico.id_ponto_turistico == self.cod_ponto_turistico
        ).first()
        lastVisit = self.dta_usuario_ponto_turistico.strftime("%d/%m/%Y, %H:%M:%S")
        userAttraction = {
            "userCode" : self.cod_usuario,
            "attractionCode" : attraction.id_ponto_turistico,
            "attractionName" : attraction.nme_ponto_turistico,
            "attractionLocal" : attraction.getLocalDict(),
            "ammountVisits" : self.qtd_visitas,
            "userAttractionImg" : self.url_img_usuario_ponto_turistico,
            "lastVisit" : lastVisit,
            "lastVisit1" : self.dta_usuario_ponto_turistico
        }
        return userAttraction