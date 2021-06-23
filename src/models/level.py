from app import db



class Level(db.Model):
    __tablename__ = 'tb_level'
    id_level  = db.Column(db.Integer, db.Sequence('tb_level_id_level_seq'), primary_key=True)
    nme_level = db.Column(db.String(50), nullable=False)
    qtd_experiencia = db.Column(db.Integer, nullable=False)
    
    def __init__(self, nme_level=None, qtd_experiencia=None):
        self.nme_level    = nme_level
        self.qtd_experiencia = qtd_experiencia
    
    def toDict(self):
        level = {
            'level' : self.id_level,
            'desc' : self.nme_level,
            'totalExp' : self.qtd_experiencia
        }
        return level

    def __str__(self):
        
        return self.toDict()                                                                                        
    
