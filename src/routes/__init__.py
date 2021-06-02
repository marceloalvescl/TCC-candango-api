from flask import Blueprint
from flask_cors import CORS

candango_routes = Blueprint('candango', __name__)
CORS(candango_routes)