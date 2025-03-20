from flask import Flask, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)


with open("C:\\Users\\Windows 10\\Desktop\\Sprint\\Entregáveis\\meu_modelo_serializado.pickle", 'rb') as f:
    modelo = pickle.load(f)


@app.route('/prever', methods=['GET'])
def prever():
    
    parametro1 = float(request.args.get('ID'))
    parametro2 = float(request.args.get('VALOR')) if request.args.get('VALOR') is not None else 0.0
    parametro3 = float(request.args.get('QUANTIDADE'))


    entrada = np.array([[parametro1, parametro2, parametro3]])
    resultado = modelo.predict(entrada)

    return jsonify({'Marca': resultado.tolist()})

if __name__ == '__main__':
    print("Servidor Flask em execução")
    app.run(debug=True)