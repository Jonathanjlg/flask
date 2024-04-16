#vou importar a classe Flask do pacote flask
from flask import Flask
from dados import Materias
#FIXME: Flask e um classe
#instãncianfo o objeto app 
#Assume o nome da aplicação como nome padrão 

app = Flask("__name__")
#NOTE: vamos decorar
#decorators
#será que o flack consegue entender essa função solta ia?
#POST(ins )


@app.route('/materias', methods = ['GET'])
def get_materias():
    return Materias











#executar a API
app.run()

