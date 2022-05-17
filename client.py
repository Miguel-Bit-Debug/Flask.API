import requests

data = {'username': 'Maria', 'secret':'@dmin', 'info':'salario', 'value':5000}

response = requests.post('http://localhost:5000/informations', data=data)
if response.status_code == 200:
    print(response.json())
else:
    print(response.status_code)