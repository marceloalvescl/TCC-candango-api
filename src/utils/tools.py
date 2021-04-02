from utils.constants import (REGEX_PARENTHESES)
import re
from db import queries


def get_keys(sql):

    keys = re.search(REGEX_PARENTHESES, sql)

    keys = keys[1].split(',')

    return keys

'''
    Author: Marcelo

    Recupera quais colunas são selecionadas em um select
        Exemplo:
            sql = select id_ponto_turistico, nme_ponto_turistico from tb_ponto_turistico ...
            Retorno:
            ['id_ponto_turistico', 'nme_ponto_turistico']
'''
def get_list_of_fields(query):
    fields = query[query.find('select')+7:query.find('from')]
    lista = fields.split(',')
    
    listOfFields = []
    for field in lista:
        listOfFields.append(field.strip())
    return listOfFields

def elements_to_dict(content, query):    
    try:
        listOfFields = tools.get_list_of_fields(query)
        listIndex = 0
        newContent = []
        for pontoTuristico in content:
            dictDetalhe = {}
            for detalhe in pontoTuristico:
                dictDetalhe[listOfFields[listIndex].strip()] = detalhe
                listIndex += 1
            newContent.append(dictDetalhe)
            listIndex = 0
        return newContent
    except Exception as e:
        print(e)
        return content

