from models.tipo_turistico import TipoTuristico
from models.local import Local
from app import db
import json
from sqlalchemy.orm import relationship

class PontoTuristico(db.Model):
    __tablename__ = 'tb_ponto_turistico'
    id_ponto_turistico  = db.Column(db.Integer, db.Sequence('tb_ponto_turistico_id_ponto_turistico_seq'), primary_key=True)
    micro_ponto_turistico = db.Column(db.Boolean, nullable=False)
    cod_ponto_turistico_pai = db.Column(db.Integer, nullable=True)
    nme_ponto_turistico = db.Column(db.String(100), nullable=False)
    dsc_ponto_turistico = db.Column(db.Text, nullable=False)
    url_img_ponto_turistico = db.Column(db.Text, nullable=True)
    qtd_experiencia = db.Column(db.Boolean, nullable=False)
    
    cod_tipo_turistico = db.Column(db.Integer, db.ForeignKey('td_tipo_turistico.id_tipo_turistico'))
    ponto_turistico = relationship(TipoTuristico, back_populates="pontos_turisticos_rel")
    cod_local = db.Column(db.Integer, db.ForeignKey('tb_local.id_local'))
    ponto_turistico_local = relationship(Local, back_populates="pontos_turisticos_rel")

    def __init__(self, micro_ponto_turistico=None,cod_ponto_turistico_pai=None,nme_ponto_turistico= None, dsc_ponto_turistico= None, url_img_ponto_turistico=None, qtd_experiencia= None, cod_tipo_turistico= None, cod_local= None):
        self.micro_ponto_turistico    = micro_ponto_turistico
        self.cod_ponto_turistico_pai    = cod_ponto_turistico_pai
        self.nme_ponto_turistico    = nme_ponto_turistico
        self.dsc_ponto_turistico    = dsc_ponto_turistico
        self.url_img_ponto_turistico = url_img_ponto_turistico
        self.qtd_experiencia = qtd_experiencia
        self.cod_tipo_turistico = cod_tipo_turistico
        self.cod_local = cod_local

    def toJson(self):
        local = { 'Endereco': self.ponto_turistico_local.end_ponto_turistico,
                  'CEP':self.ponto_turistico_local.cep_ponto_turistico,
                  'Latitude':self.ponto_turistico_local.geo_lat_ponto_turistico,
                  'Longitude':self.ponto_turistico_local.geo_long_ponto_turistico
                }
                
        ponto_turistico = {
            'id': self.id_ponto_turistico,
            'detalhes': {
                'Nome': self.nme_ponto_turistico,
                'Micro Ponto':self.micro_ponto_turistico, 
                'Cod Ponto Pai': self.cod_ponto_turistico_pai,
                'Descrição': self.dsc_ponto_turistico, 
                'Url Imagem': self.url_img_ponto_turistico,
                'Experiência': self.qtd_experiencia,
                'Cod Tipo': self.cod_tipo_turistico, 
                'Cod Local': self.cod_local, 
                'Local': local 
            }
        }

        return json.dumps(ponto_turistico)

    def __str__(self):
        return str(self.toJson())                                                                                        
    
