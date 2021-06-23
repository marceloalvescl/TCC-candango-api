from settings import logger, server_configuration
from app import app

if __name__ == '__main__':
    server_config = server_configuration()
    logger.info("Inicializando o serviço de backend Candango...")
    logger.info(f"Configurações do serviço: {server_config}")
    logger.info("CandanGO API inicializado e pronta para uso!")
    try:
        app.run(host="127.0.0.1", port=int(server_config["HttpPort"]), debug=True)
    except Exception as e:
        pass