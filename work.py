import requests

# идентификация
def get_identification(token, my_login):
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' + token
    res = s.get('https://edge.qiwi.com/identification/v1/persons/' + my_login + '/identification')
    return res.json()

#req = requests.get('https://qiwi.com/main/')
token = 'xxx'
login = 'test'
jsObject = get_identification(token, login)
print('json=' + jsObject)
