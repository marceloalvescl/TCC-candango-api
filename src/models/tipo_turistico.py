from app import db
from sqlalchemy.orm import relationship



class TipoTuristico(db.Model):
    __tablename__ = 'td_tipo_turistico'
    id_tipo_turistico  = db.Column(db.Integer, db.Sequence('td_tipo_turistico_id_tipo_turistico_seq'), primary_key=True)
    dsc_tipo_turistico = db.Column(db.String(50), nullable=False)
    pontos_turisticos_rel = relationship("PontoTuristico")
    
    def __init__(self, dsc_tipo_turistico=None):
        self.dsc_tipo_turistico    = dsc_tipo_turistico
        
    def __str__(self):
        pontos_turisticos_relacionados = "[\n"
        for ponto_turistico in self.pontos_turisticos_rel:
            pontos_turisticos_relacionados += "Id={0}\nNome={1}\n".format(ponto_turistico.id_ponto_turistico, ponto_turistico.nme_ponto_turistico)
        pontos_turisticos_relacionados += "]"
        tipo_turistico = '''id={0}: [descrição={1}, Pontos Turisticos Relacionados: {2} ]'''.format(
                                                    self.id_tipo_turistico, self.dsc_tipo_turistico, pontos_turisticos_relacionados)
        return tipo_turistico                                                                                        
    
