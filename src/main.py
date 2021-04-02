from settings import logger, server_configuration
from views.routes import Routes, candango_routes
from flask_cors import CORS
from flask import Flask

app = Flask(__name__)
app.register_blueprint(candango_routes)


CORS(app, automatic_options=True)

if __name__ == '__main__':
    server_config = server_configuration()

    logger.info("Inicializando o serviço de backend Candango...")
    logger.info(f"Configurações do serviço: {server_config}")

    logger.info("CandanGO API inicializado e pronta para uso!")
    try:
        app.run(host="127.0.0.1", port=int(server_config["HttpPort"]), debug=True)
    except:
        print("Error")