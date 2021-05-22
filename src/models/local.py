from app import db
from sqlalchemy.orm import relationship

class Local(db.Model):
    __tablename__ = 'tb_local'
    id_local  = db.Column(db.Integer, db.Sequence('tb_local_id_local_seq'), primary_key=True)
    end_ponto_turistico = db.Column(db.String(150), nullable=False)
    cep_ponto_turistico = db.Column(db.String(9), nullable=False)
    geo_lat_ponto_turistico = db.Column(db.String(10), nullable=False)
    geo_long_ponto_turistico = db.Column(db.String(10), nullable=False)

    pontos_turisticos_rel = relationship("PontoTuristico")
    
    def __init__(self, end_ponto_turistico=None,cep_ponto_turistico=None,geo_lat_ponto_turistico= None, geo_long_ponto_turistico= None ):
        self.end_ponto_turistico    = end_ponto_turistico
        self.cep_ponto_turistico    = cep_ponto_turistico
        self.geo_lat_ponto_turistico    = geo_lat_ponto_turistico
        self.geo_long_ponto_turistico    = geo_long_ponto_turistico
        
    def __str__(self):
        local = '''id={0}: [Endereço={1}, CEP={2}, Latitude: {3}, Longitude: {4}, Ponto Turisticos Relacionados: {5}]'''.format(
                                                    self.id_local, self.end_ponto_turistico,self.cep_ponto_turistico,self.geo_lat_ponto_turistico, self.geo_long_ponto_turistico, self.pontos_turisticos_rel)
        return local                                                                                        
    