from app import db

class Circuito(db.Model):
    __tablename__ = 'tb_circuito'
    id_circuito  = db.Column(db.Integer, db.Sequence('tb_circuito_id_circuito_seq'), primary_key=True)
    nme_circuito = db.Column(db.String(75), nullable=False)
    qtd_experiencia = db.Column(db.Integer, nullable=False)
    
    def __init__(self, dsc_tipo_desafio=None, qtd_experiencia = None):
        self.dsc_tipo_desafio    = dsc_tipo_desafio
        self.qtd_experiencia = qtd_experiencia
        
    def __str__(self):
        circuito = '''id={0}: [Nome: {1}, Experiência: {2} ]'''.format(
                                                    self.id_circuito, self.nme_circuito, self.qtd_experiencia)
        return circuito                                                                                        
    
