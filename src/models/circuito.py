from app import db
from models.circuito_ponto_turistico import CircuitoPontoTuristico
from models.ponto_turistico import PontoTuristico



class Circuito(db.Model):
    __tablename__ = 'tb_circuito'
    id_circuito  = db.Column(db.Integer, db.Sequence('tb_circuito_id_circuito_seq'), primary_key=True)
    nme_circuito = db.Column(db.String(75), nullable=False)
    qtd_experiencia = db.Column(db.Integer, nullable=False)
    dsc_circuito = db.Column(db.Text)

    def __init__(self, nme_circuito=None, qtd_experiencia = None, dsc_circuito=None):
        self.nme_circuito    = nme_circuito
        self.qtd_experiencia = qtd_experiencia
        self.dsc_circuito    = dsc_circuito
        
    def __str__(self):
        return str(self.toDict())
    
    def toDict(self):
        circuitAttractions = CircuitoPontoTuristico.query.filter(CircuitoPontoTuristico.cod_circuito == self.id_circuito).all()
        attractions = []
        for circuitAttraction in circuitAttractions:
            attraction = PontoTuristico.query.filter(PontoTuristico.id_ponto_turistico == circuitAttraction.cod_ponto_turistico).first()
            attractions.append(attraction.toDict())
        circuitos = {
            'circuitId'   : self.id_circuito,
            'circuitName' : self.nme_circuito,
            'circuitDesc' : self.dsc_circuito,
            'ammountExp'  : self.qtd_experiencia,
            'attractions' : attractions
        }
        return circuitos
