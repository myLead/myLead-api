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

    if users == None:
        return jsonify({'status': 'error', 'message': 'Sem ocorrencias', 'data': {}})
    else:       
        return jsonify({'status': 'success', 'message': 'Lista de usuarios', 'data': users})

@app.route('/user/<id>' , methods = ['GET'])
def get_one_user(id):

    user = userController.list_one_user(id)
    if user == None:
        return jsonify({'status': 'error', 'message': 'Sem ocorrencias', 'data': {}})
    else:       
        return jsonify({'status': 'success', 'message': 'Usuario encontrado', 'data': user})

@app.route('/user', methods =['POST']) 
def create_user():
    
    data = request.get_json()

    teste = data['senha_usuario']
    passw = hashlib.md5()
    passw.update(teste.encode('utf-8'))
    hash = passw.hexdigest()
    
    new_user = Usuario(nome=data['nome'], email_usuario = data['email_usuario'],senha_usuario=hash, cnpj=data['cnpj'])
    oper_result = userController.create_user(new_user)

    if oper_result == None:
    
        return jsonify({'status': 'success', 'message': 'Usuario cadastrado', 'data': {}})

    else:
        return jsonify({'status': 'error', 'message': 'Email ja cadastrado', 'data': {} })

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    email_usuario = data['email_usuario']

    teste = data['senha_usuario']
    passw = hashlib.md5()
    passw.update(teste.encode('utf-8'))
    hash = passw.hexdigest()

    user = userController.verify_user(hash, email_usuario)
    
    if user == None:
        return jsonify({'status': 'error', "message": "Senha ou email incorretos", 'data': {}})
    else:    
        return jsonify({'status': 'success', "message": "Uma ocorrencia encontrada", 'data': user})

@app.route('/user/<id>', methods = ['DELETE'])
def delete_user(id):

    open_result = userController.delete_user(id)

    if open_result == None:
        return jsonify({'status': 'error', 'message': 'Usuario nao encontrado', 'data': {}})
    else:
        return jsonify({'status': 'success', 'message': 'Usuario deletado', 'data': {}})
