from app import db
import json

class Medalha(db.Model):
    __tablename__ = 'tb_medalha'
    id_medalha  = db.Column(db.Integer, db.Sequence('tb_medalha_id_medalha_seq'), primary_key=True)
    nme_medalha = db.Column(db.String(75), nullable=False)
    url_img_medalha = db.Column(db.Text, nullable=True)
    qtd_experiencia = db.Column(db.Integer, nullable=True)
    
    def __init__(self, id_medalha=None, nme_medalha=None, url_img_medalha=None, qtd_experiencia=None):
        self.id_medalha  = id_medalha
        self.nme_medalha = nme_medalha
        self.url_img_medalha = url_img_medalha
        self.qtd_experiencia = qtd_experiencia
    
    def toJson(self):
        medalha = {
            'Nome': self.nme_medalha,
            'UrlImagem':self.url_img_medalha,
            'QtdExperiencia':self.qtd_experiencia
        }

        return json.dumps(medalha)

    def toDict(self):
        medalha = {
            'Nome': self.nme_medalha,
            'UrlImagem':self.url_img_medalha,
            'QtdExperiencia':self.qtd_experiencia
        }
        return medalha

    def __str__(self):
        return str(self.toJson())       