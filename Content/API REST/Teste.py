import requests


url = 'http://127.0.0.1:5000/prever'

dict_json = {
    'ID': 1,
    'VALOR(R&)': 3299.0,
    'QUANTIDADE': 50
}

response = requests.get(url, params=dict_json)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Erro: {response.status_code}")
