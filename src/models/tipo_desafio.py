from app import db

class TipoDesafio(db.Model):
    __tablename__ = 'td_tipo_desafio'
    id_tipo_desafio  = db.Column(db.Integer, db.Sequence('td_tipo_desafio_id_tipo_desafio_seq'), primary_key=True)
    dsc_tipo_desafio = db.Column(db.String(100), nullable=False)
    
    def __init__(self, dsc_tipo_desafio=None):
        self.dsc_tipo_desafio    = dsc_tipo_desafio
        
    def __str__(self):
        tipo_desafio = '''id={0}: [descrição={1}, ]'''.format(
                                                    self.id_tipo_desafio, self.dsc_tipo_desafio)
        return tipo_desafio                                                                                        
    
