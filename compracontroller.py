from flask import Flask, request, jsonify, render_template
from  dbhelp import *
import hashlib

app = Flask(__name__)


@app.route('/compra', methods=['GET'])
def get_all_users():

    compras = Compra.query.all()

    output = []

    for compra in compras:
        user_data = {}
        user_data['id_compra'] = compra.id_compra
        user_data['data_compra'] = compra.data_compra
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
    print(teste)
    passw = hashlib.md5()
    passw.update(teste.encode('utf-8'))
    hash = passw.hexdigest()
    print(hash)
    new_user = Usuario(nome=data['nome'], email_usuario = data['email_usuario'],senha_usuario=hash, cnpj=data['cnpj'])
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message' : 'New user created!'})

@app.route('/user/<use_id>', methods=['put'])
def promote_user():
    return ''

@app.route('/user/<id>', methods = ['DELETE'])
def delete_user(id):

    user = Usuario.query.filter_by(id_usuario=id ).first()
    if not user:
        return jsonify({'messege' : 'No user found"'})
    db.session.delete(user)
    db.session.commit()
    return jsonify({'messege' : 'User has been Deleted" '})


if __name__ == '__main__':
    app.run(debug=True)
    

