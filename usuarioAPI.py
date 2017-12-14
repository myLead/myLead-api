from flask import Flask, request, jsonify, render_template
from  dbhelper import *
from flask_sqlalchemy import SQLAlchemy
import hashlib
from mylead import app, db
from controller.usuariocontroller import *

userController = UsuarioController()

@app.route('/user', methods=['GET'])
def get_all_users():

    users = userController.list_user()

    return jsonify({'users' : users})

@app.route('/user/<id>' , methods = ['GET'])
def get_one_user(id):

    user = userController.list_one_user(id)

    return jsonify({'user' : user})

@app.route('/user', methods =['POST'])
def create_user():
    
    data = request.get_json()

    teste = data['senha_usuario']
    passw = hashlib.md5()
    passw.update(teste.encode('utf-8'))
    hash = passw.hexdigest()
    
    new_user = Usuario(nome=data['nome'], email_usuario = data['email_usuario'],senha_usuario=hash, cnpj=data['cnpj'])
    oper_result = userController.create_user(new_user)
    return jsonify(oper_result)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    email_usuario = data['email_usuario']

    teste = data['senha_usuario']
    passw = hashlib.md5()
    passw.update(teste.encode('utf-8'))
    hash = passw.hexdigest()

    user = userController.verify_user(hash, email_usuario)

    # if not user:
    #     return jsonify({'status':'error','message': 'Senha ou email invalidos', 'ata': {}})
    
    # user_data = {}
    # user_data['nome'] = user.nome
    # user_data['email_usuario'] = user.email_usuario
    # user_data['senha_usuario'] = user.senha_usuario

    return jsonify({'status': 'success', 'data': user, "message": "Uma ocorrência encontrada"})

@app.route('/user/<id>', methods = ['DELETE'])
def delete_user(id):

    open_result = userController.delete_user(id)
    return jsonify(open_result)