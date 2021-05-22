from app import db

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
    ponto_turistico = db.relationship("TipoTuristico", back_populates="pontos_turisticos_rel")
    cod_local = db.Column(db.Integer, db.ForeignKey('tb_local.id_local'))
    ponto_turistico_local = db.relationship("Local", back_populates="pontos_turisticos_rel")
    
    def __init__(self, micro_ponto_turistico=None,cod_ponto_turistico_pai=None,nme_ponto_turistico= None, dsc_ponto_turistico= None, url_img_ponto_turistico=None, qtd_experiencia= None, cod_tipo_turistico= None, cod_local= None):
        self.micro_ponto_turistico    = micro_ponto_turistico
        self.cod_ponto_turistico_pai    = cod_ponto_turistico_pai
        self.nme_ponto_turistico    = nme_ponto_turistico
        self.dsc_ponto_turistico    = dsc_ponto_turistico
        self.url_img_ponto_turistico = url_img_ponto_turistico
        self.qtd_experiencia = qtd_experiencia
        self.cod_tipo_turistico = cod_tipo_turistico
        self.cod_local = cod_local
        
    def __str__(self):
        ponto_turistico = '''id={0}: [Micro Ponto={1}, Cod Ponto Pai={2}, Nome: {3}, Descrição: {4}, Url Imagem: {5}, Experiência: {6}, Cod Tipo: {7}, Cod Local: {8} ]'''.format(
                                                    self.id_ponto_turistico, self.micro_ponto_turistico, self.cod_ponto_turistico_pai, self.nme_ponto_turistico, self.dsc_ponto_turistico, self.url_img_ponto_turistico, self.qtd_experiencia, self.cod_tipo_turistico, self.cod_local )
        return ponto_turistico                                                                                        
    
