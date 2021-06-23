from app import db


'''
    Classe responsável pela tabela associativa: ta_circuito_ponto_turistico
        Um circuito pode ter vários pontos turísticos
        Um ponto turístico pode estar em vários circuitos
    Atributos:
    ----------
    cod_circuito : int foreign key
        Chave estrangeira referenciado a chave primária:id_circuito da tabela básica: tb_circuito
        Chave estrangeira referenciado a chave primária:id_ponto_turistico da tabela básica: tb_ponto_turistico
        
'''
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