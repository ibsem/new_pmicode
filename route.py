from flask import Flask,request
#pip install flask

app = Flask(__name__)

#   logins

@app.route("/login_usuario", methods=['GET'])
def login_usuario():
    data = request.json


@app.route("/login_funcionario", methods=['GET'])
def login_func():
    data = request.json


@app.route("/login_gestor", methods=['GET'])
def login_gestor():
    data = request.json


 #  chamados

@app.route("/meu_chamado_ti",methods=['POST'])
def chamado_ti():
    data = request.json


@app.route("/meu_chamado_papelaria",methods=['POST'])
def chamado_pape():
    data = request.json



# cadastros

@app.route("/cadastro_usuario", methods=['POST'])
def cadastro_usuario():
    data = request.json


@app.route("/cadastro_gestor", methods=['POST'])
def cadastro_gestor():
    data = request.json


@app.route("/cadastro_funcionario", methods=['POST'])
def cadastro_func():
    data = request.json

# listar chamado

@app.route("/meu_chamado_ti/<id>", methods=['GET'])#lsitar
def get(id):


@app.route("/meu_chamado_ti_funcionario/<id>", methods=['GET'])#lsitar
def get(id):


@app.route("/meu_chamado_papelaria/<id>", methods=['GET'])#lsitar
def get(id):


@app.route("/meu_chamado_papelaria_funcionario/<id>", methods=['GET'])
def get(id):


#atualizar

@app.route("/atualizar_chamado_ti/<id>", methods=['PUT'])#atualisa
def put(id):
    data = request.json


@app.route("/atualizar_chamado_papelaria/<id>", methods=['PUT'])#atualisa
def put(id):
    data = request.json


#deleta

@app.route("/apagar_meu_chamado_ti/<id>", methods=['DELETE'])#deleta
def delete(id):



@app.route("/apagar_meu_chamado_papelaria/<id>", methods=['DELETE'])#deleta
def delete(id):
