from flask                        import Flask, request, jsonify, session, g, render_template
from dbhelper                     import *
from flask_sqlalchemy             import SQLAlchemy
from mylead                       import app, db
from controller.usuariocontroller import *
from controller.compracontroller  import *
from controller.csvcontroller import *
from utils                        import Utils
import os
import hashlib

userController   = UsuarioController()
compraController = CompraController()
csvController =  CsVController()
utils            = Utils()

@app.route('/users', methods=['GET'])
def get_all_users():
    users = userController.list_user()
   
    if users == None:
        return jsonify({'status': 'error', 'message': 'Sem ocorrencias', 'data': {}})
    else:

        output = []

        for user in users:

            user_data                  = {}
            user_data['id_usuario']    = user.id_usuario
            user_data['nome']          = user.nome
            user_data['email_usuario'] = user.email_usuario
            user_data['senha_usuario'] = user.senha_usuario
            user_data['cnpj']          = user.cnpj
            user_data['create_at']     = user.create_at

            output.append(user_data)

        return jsonify({'status': 'success', 'message': 'Lista de usuarios', 'data': output})
  

@app.route('/user/<id>' , methods = ['GET'])
def get_one_user(id):
    user = userController.list_one_user(id)
    
    if user == None:
        return jsonify({'status': 'error', 'message': 'Sem ocorrencias', 'data': {}})
    else:

        user_data = {}
        user_data['id_usuario']    = user.id_usuario
        user_data['nome']          = user.nome
        user_data['email_usuario'] = user.email_usuario
        user_data['senha_usuario'] = user.senha_usuario
        user_data['cnpj']          = user.cnpj
        user_data['create-at']     = user.create_at

        return jsonify({'status': 'success', 'message': 'Usuario encontrado', 'data': user_data})


@app.route('/users', methods =['POST']) 
def create_user(): 
    data  = request.get_json()

    teste = data['senha_usuario']
    passw = hashlib.md5()

    passw.update(teste.encode('utf-8'))
    hash = passw.hexdigest()
    
    new_user    = Usuario(nome = data['nome'], email_usuario = data['email_usuario'], senha_usuario = hash, cnpj = data['cnpj'])
    verificarEmail = userController.verify_user_by_email(data['email_usuario'])
    if verificarEmail == None:
        
        saveUser = userController.create_user(new_user)

        today      = utils.getDateToday()
        vencimento = utils.getDateFuture()
        lastUser   = userController.getLast()
        new_order  = Compra(data_compra = today, data_vencimento = vencimento, id_usuario = lastUser, id_plano = data['id_plano'])
        order      = compraController.createComopra(new_order)
        # essa condicao garantirá que ao salvar um usuario ele levará consigo
        # as informações referentes a compra do usuario como tipo de plano e id do usuario

        return jsonify({'status': 'success', 'message': 'Usuario cadastrado', 'data': {}})

    else:
        return jsonify({'status': 'error', 'message': 'Email ja cadastrado', 'data': {}})


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
        user_data                  = {}
        user_data['id_usuario']    = user.id_usuario
        user_data['nome']          = user.nome
        user_data['email_usuario'] = user.email_usuario
        session['user'] = str(user.id_usuario)
        return  jsonify({'status': 'success', "message": "Usuário Logado com Sucesso", 'data': user_data})


@app.before_request
def before_request():
    g.user = None
    if 'user' in session:
        g.user = session['user']

@app.route('/getsession', methods = ['GET'])
def getsession():
    if 'user' in session:
        return session['user']

    return 'Not logged in!'


@app.route('/logout', methods=['GET'])
def logout():
    session.pop('user', None)
    return 'Logout!'

@app.route('/user/<id>', methods = ['DELETE'])
def delete_user(id):
    open_result = userController.delete_user(id)

    if open_result == None:
        return jsonify({'status': 'error', 'message': 'Usuario nao encontrado', 'data': {}})
    else:
        return jsonify({'status': 'success', 'message': 'Usuario deletado', 'data': {}})

@app.route('/upload', methods = ['POST'])
def upload():
    file = request.files['inputFile']
    file_name = file.filename
    file_path = os.path.join("TMP_DIR", file_name)
    file.save(file_path)
    csv_to_jspn = utils.csvToJson(file_path)
    id_usuario =int(getsession())
    newCsv = CsvFile(id_usuario=1,
                     csvjson=csv_to_jspn, csvblob=file.read())
    upLoadFile = csvController.createBaseCsv(newCsv)
    return jsonify({'status': 'success', 'message': 'Upload completo', 'data': {}})