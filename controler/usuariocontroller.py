from flask import Flask, request, jsonify, render_template
from  dbhelp import Usuario
from flask_sqlalchemy import SQLAlchemy
import hashlib
from mylead import app, db

# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://matyyaxexjsmlg:8107604602e55661da27d1cac9e0ab04651a87ac4e6846101ca391cb383199c3@ec2-107-20-176-7.compute-1.amazonaws.com:5432/de7q9p7jklnn70'
# app.debug = True
# db = SQLAlchemy(app)
# db.init_app(app)

# @app.route('/create')
# def create():
#     db.create_all()
#     return 'Tablelas criadas'

# @app.route('/')
# def index():
#     return render_template('index.html')

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
    
    usuarioexistente = Usuario.query.filter_by(email_usuario=data['email_usuario']).first()
    
    if not usuarioexistente:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'New user created!'})

    return jsonify({'message' : 'Usuario já cadastrado'})


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
    

