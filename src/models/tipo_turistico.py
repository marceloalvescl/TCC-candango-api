from app import db


class TipoTuristico(db.Model):
    __tablename__ = 'td_tipo_turistico'
    id_tipo_turistico  = db.Column(db.Integer, db.Sequence('td_tipo_turistico_id_tipo_turistico_seq'), primary_key=True)
    dsc_tipo_turistico = db.Column(db.String(50), nullable=False)
    pontos_turisticos_rel = db.Relationship("PontoTuristico")
    
    def __init__(self, dsc_tipo_turistico=None):
        self.dsc_tipo_turistico    = dsc_tipo_turistico
        
    def __str__(self):
        tipo_turistico = '''id={0}: [descrição={1}, Pontos Turisticos Relacionados: {2} ]'''.format(
                                                    self.id_tipo_turistico, self.dsc_tipo_turistico, self.pontos_turisticos_rel)
        return tipo_turistico                                                                                        
    
