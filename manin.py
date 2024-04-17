#vou importar a classe Flask do pacote flask
#o Make_reponse geralmente gera em JSON
from flask import Flask,make_response,jsonify,request
from dados import Materias
#FIXME: Flask e um classe
#instãncianfo o objeto app 
#Assume o nome da aplicação como nome padrão 

app = Flask("__name__")
#NOTE: vamos decorar
#decorators
#será que o flack consegue entender essa função solta ia?


@app.route('/materias', methods = ['GET'])
def get_materias():
    return make_response    (   jsonify (   Materias    )      ) 


@app.route("/")
def index():
    return "Projeto Integrador Base (Enem)"




#request
#POST
@app.route('/materias',methods=['POST'])
def create_materia():
    Materia = request.json
    return Materia



#executar a API
app.run()