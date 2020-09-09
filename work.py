import requests

# идентификация
def get_identification(token, my_login):
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' + token
    res = s.get('https://edge.qiwi.com/identification/v1/persons/' + my_login + '/identification')
    return res.json()

# не стоит сохранять персональные данные в коде (читай из файла, переменных окружения, вводи явно в программу)
token = 'xxx'
login = 'test'
jsObject = get_identification(token, login)
print('json=' + jsObject)
