from flask import Flask, request, jsonify, render_template
from  dbhelp import Usuario
from flask_sqlalchemy import SQLAlchemy
import hashlib
from mylead import app, db
from controler.usuariocontroller import *

userController = UsuarioController()

@app.route('/user', methods=['GET'])
def get_all_users():

    users = Usuario.query.all()

    output = []

    for user in users:
        user_data = {}
        user_data['id_usuario'] = user.id_usuario
        user_data['nome'] = user.nome
        user_data['email_usuario'] = user.email_usuario
        user_data['senha_usuario'] = user.senha_usuario
        user_data['cnpj'] = user.cnpj
        user_data['create_at'] = user.create_at
        output.append(user_data)

    return jsonify({'users' : output})

@app.route('/user/<id>' , methods = ['GET'])
def get_one_user(id):

    user = Usuario.query.filter_by(id_usuario=id).first()

    if not user:
        return jsonify({'messege' : 'No user found!'})
    
    user_data = {}
    user_data['id_usuario'] = user.id_usuario
    user_data['nome'] = user.nome
    user_data['email_usuario'] = user.email_usuario
    user_data['senha_usuario'] = user.senha_usuario
    user_data['cnpj'] = user.cnpj
    user_data['create_at'] = user.create_at

    return jsonify({'user' : user_data})

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
    valors = {}
    valors['email_usuario'] = email_usuario
    valors['senha_usuario'] = hash

    user = Usuario.query.filter_by(email_usuario=data['email_usuario'], senha_usuario=hash).first()

    if not user:
        return jsonify({'status':'error','message': 'Senha ou email invalidos', 'data': {}})
    
    user_data = {}
    user_data['nome'] = user.nome
    user_data['email_usuario'] = user.email_usuario
    user_data['senha_usuario'] = user.senha_usuario

    return jsonify({'status': 'success', 'data': user_data, "message": "Uma ocorrência encontrada"})

@app.route('/user/<id>', methods = ['DELETE'])
def delete_user(id):

    user = Usuario.query.filter_by(id_usuario=id).first()
    if not user:
        return jsonify({'message' : 'No user found"'})
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message' : 'User has been Deleted" '})


# if __name__ == '__main__':
#     app.run(debug=True)
    

