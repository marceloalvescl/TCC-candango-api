import logging
import os
from utils.constants import DB_CREDENTIALS


def server_configuration():
    """
    Preenche o parâmetro config com variáveis de ambiente
        pré-determinadas.
    A função tenta carregar o valor da variável de ambiente ou, se ela não
    estiver definida, carrega um valor padrão.

    Por exemplo: o comando os.environ.get('HTTP_PORT', 8080) carrega a
    variável HTTP_PORT ou o valor padrão 8080.

    """

    logging.debug("Carregando as variáveis de ambiente")
    config = dict()
    config["Debug"] = "True"
    config["HttpPort"] = int(os.environ.get('HTTP_PORT', '5001'))
    config["HttpsPort"] = int(os.environ.get('HTTPS_PORT', '8443'))
    config['DatabaseHost'] = DB_CREDENTIALS['DatabaseHost']
    config['DatabaseName'] = DB_CREDENTIALS['DatabaseName']
    config["DatabasePort"] = DB_CREDENTIALS['DatabasePort']
    config['DatabaseUser'] = DB_CREDENTIALS['DatabaseUser']
    config['DatabasePassword'] = DB_CREDENTIALS['DatabasePassword']

    return config

logging.basicConfig(
    format=('%(asctime)s,%(msecs)-3d - %(name)-12s - %(levelname)-8s => '
            '%(message)s'),
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.DEBUG
)

logger = logging.getLogger(__name__)
