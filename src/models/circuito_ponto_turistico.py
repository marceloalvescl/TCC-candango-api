from app import db


class CircuitoPontoTuristico(db.Model):
    __tablename__ = 'ta_circuito_ponto_turistico'
    id_circuito_ponto_turistico  = db.Column(db.Sequence('ta_circuito_ponto_turistico_id_circuito_ponto_turistico_seq'), primary_key=True)
    cod_circuito = db.Column(db.Integer, db.ForeignKey('tb_circuito.id_circuito'))
    cod_ponto_turistico = db.Column(db.Integer, db.ForeignKey('tb_ponto_turistico.id_ponto_turistico'))

    def __init__(self, cod_circuito=None, cod_ponto_turistico=None):
        self.cod_circuito = cod_circuito
        self.cod_ponto_turistico = cod_ponto_turistico

    def toDict(self):
        circuitoPontoTuristico = {
            "codCircuito" : self.cod_usuario,
            "attractions" : self.attractions
        }
        return circuitoPontoTuristico