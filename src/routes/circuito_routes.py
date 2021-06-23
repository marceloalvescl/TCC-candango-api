from flask import request
from flask_login import login_required
from routes import candango_routes
from controllers import circuito_controller  

# Rota /api/candango/circuits - Método GET
# ["GET"] para buscar todos os circuitos
@candango_routes.route('/circuit', methods=['GET'])
@login_required
def candango_circuitos():
    return circuito_controller.getAllCircuits()

# Rota /api/candango/circuits/user - Método POST
# ["POST"] para completar circuito de um usuário
@candango_routes.route('/circuit/user', methods=['POST'])
@login_required
def candango_circuitos_usuario():
    if request.json:
        return circuito_controller.userCompletedCircuit(request.json)
    else:
        return {"error" : "Favor enviar JSON na request"}, 400        

