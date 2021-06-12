from app import db
from models.ponto_turistico import PontoTuristico
from models.local import Local

def getAllPontosTuristicos():
    pontosTuristicos = db.session.query(PontoTuristico).join(Local).all()
    listaPontosTuristicos = {"pontos turisticos" : []}
    for pontoTuristico in pontosTuristicos:
        listaPontosTuristicos["pontos turisticos"].append(pontoTuristico.toDict())
    print(listaPontosTuristicos)
    return listaPontosTuristicos, 200