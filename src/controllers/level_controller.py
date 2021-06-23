from app import db
from models.level import Level

def addExp(usuario, incomingExp):
    levelAtual = Level.query.filter(
        Level.id_level == usuario.cod_level
    ).first()

    if(levelAtual.qtd_experiencia < (incomingExp + usuario.qtd_exp_atual)):
        usuario.cod_level += 1
        usuario.qtd_exp_atual = 0
    else:
        usuario.qtd_exp_atual += incomingExp
    db.session.add(usuario)
    db.session.commit()
    db.session.refresh(usuario)

def getLevelById(codLevel):
    level = Level.query.filter(Level.id_level == codLevel).first()
    return level.toDict()