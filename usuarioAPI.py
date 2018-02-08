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

app.secret_key = os.urandom(24)

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
        return  jsonify({'status': 'success', "message": "Usuário Logado com Sucesso", 'data': user_data})



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
    newCsv = CsvFile(id_usuario=1,
                     csvjson=csv_to_jspn, csvblob=file.read())
    upLoadFile = csvController.createBaseCsv(newCsv)
    return jsonify({'status': 'success', 'message': 'Upload completo', 'data': {}})


@app.route('/resultados', methods=['POST' , 'GET'])
def teste():
    if request.method == 'POST':

        data = request.get_json()

        alimentar = Resultados(Usuario=data['Usuario'], Qtde_Clientes=data[
            'Qtde_Clientes'], Qtde_Leads=data['Qtde_Leads'], Qtde_Superleads=data['Qtde_Superleads'],
            Media_Scoring_Superleads=data['Media_Scoring_Superleads'], 
            Media_Interacoes_Superleads = data['Media_Interacoes_Superleads'],
                                             Scoring_Superleads = data['Scoring_Superleads'], Interacoes_Superleads=data['Interacoes_Superleads']
            )
        db.session.add(alimentar)
        db.session.commit()

        return jsonify({'status': 'success', 'message': 'dados salvos completo', 'data': {}})

#     else:
#         datas = Resultados.query.all()

#         if datas == None:

#             return jsonify({'status': 'error', 'message': 'Sem ocorrencias', 'data': {}})

#         else:
#             output = []

#             for data in datas:

#                 teste_data = {}
#                 teste_data['id_teste'] = data.idteste
#                 teste_data['valor1'] = data.valor1
#                 teste_data['valor2'] = data.valor2
#                 teste_data['valor3'] = data.valor3
#                 teste_data['valor4'] = data.valor4
                

#                 output.append(teste_data)

#             return jsonify({'status': 'success', 'message': 'lista de teste', 'data': output})


@app.route('/resultado/<id>', methods=['GET'])
def teste_id(id):
    data = Resultados.query.filter_by(id_resultado=id).first()

    if data == None:
        return jsonify({'status': 'error', 'message': 'Sem ocorrencias', 'data': {}})
    else:

        resultado_data = {}
        resultado_data['id_resultado'] = data.id_resultado
        resultado_data['Usuario'] = data.Usuario
        resultado_data['Qtde_Clientes'] = data.Qtde_Clientes
        resultado_data['Qtde_Leads'] = data.Qtde_Leads
        resultado_data['Qtde_Superleads'] = data.Qtde_Superleads
        resultado_data['Media_Scoring_Superleads'] = data.Media_Scoring_Superleads
        resultado_data['Media_Interacoes_Superleads'] = data.Media_Interacoes_Superleads
        resultado_data['Scoring_Superleads'] = data.Scoring_Superleads
        resultado_data['Interacoes_Superleads'] = data.Interacoes_Superleads

        return jsonify({'status': 'success', 'message': 'Teste encontrado', 'data': resultado_data})
