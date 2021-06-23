from app import db
from models.circuito import Circuito
from models.circuito_ponto_turistico import CircuitoPontoTuristico
from models.usuario_circuito import UsuarioCircuito
from settings import logger
from flask_login import current_user
from controllers.attraction_controller import getUserVistedAttraction

def getAllCircuits():
    circuitos = db.session.query(Circuito).all()
    dict_circuitos = {"circuits" : []}
    for circuito in circuitos:
        dict_circuitos['circuits'].append(circuito.toDict())
    logger.info(circuitos)
    return dict_circuitos, 201

def userCompletedCircuit(requestJson):
    userVisitedAllAttractionsOfCircuit, missingVisits = verifyUserVisitedAttractionsOfCircuit(requestJson['circuitId'])
    if userVisitedAllAttractionsOfCircuit: 
        usuarioCircuito = UsuarioCircuito(
            cod_circuito=requestJson['circuitId'],
            cod_usuario=current_user.id_usuario
        )
        db.session.add(usuarioCircuito)
        db.session.commit()
        return {'msg' : 'circuito liberado pelo usuario'}, 201
    else:
        return {'msg' : 'ainda falta visitar alguns pontos turisticos para completar circuito', 
                'attractionsLeftToVist' : missingVisits}

def verifyUserVisitedAttractionsOfCircuit(circuitID):
    # get a list of attractions of a circuit
    circuitAttractions = CircuitoPontoTuristico.query.filter(CircuitoPontoTuristico.cod_circuito == circuitID).all()
    visitedAll = True
    missingVisits = []  
    for circuitAttraction in circuitAttractions:
        visitedAttraction = getUserVistedAttraction(circuitAttraction.cod_ponto_turistico)
        if not visitedAttraction:
            visitedAll = False
            missingVisits.append(circuitAttraction.cod_ponto_turistico)
    return visitedAll, missingVisits
            