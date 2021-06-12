from flask import Blueprint
from flask_cors import CORS

candango_routes = Blueprint('candango', __name__, url_prefix="/api/candango")
CORS(candango_routes) #Habilita o compartilhamento de recursos com origens diferentes CORS