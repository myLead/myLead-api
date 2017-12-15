from DAO.UsuarioDAO import *

class UsuarioController():

    def __init__(self):
        self.__userDAO = UsuarioDAO()

    
    def create_user(self, user):

        usuarioexistente = self.__userDAO.get_user_by_email(user.email_usuario)

        if usuarioexistente == None:

            self.__userDAO.create_user(user)
            return {'status': 'success', 'message': 'Usuario cadastrado', 'data': {}}

        else:
            return {'status': 'error', 'message': 'Email ja cadastrado', 'data': {}}

    def delete_user(self, id):

        user = self.__userDAO.get_user_by_id(id)
        if user == None:

            return {'status': 'error', 'message': 'Usuario nao encontrado', 'data': {}}
        else:
            self.__userDAO.delete_user(user)
            return {'status': 'sussecc', 'message': 'Usuario deletado', 'data': {}}

    def list_user(self):

        users = self.__userDAO.list()
        
        if users == None:
            return  {'status': 'error', 'message': 'Sem ocorrencias', 'data': {}}
        
        else:

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
            return {'status': 'success', 'message': 'Lista de usuarios', 'data': output}

    def list_one_user(self, id):
        user = self.__userDAO.list_one_user(id)

        if user ==None:
            return {'status': 'error', 'message': 'Sem ocorrencias', 'data': {}}
        else:

            user_data = {}
            user_data['id_usuario'] = user.id_usuario
            user_data['nome'] = user.nome
            user_data['email_usuario'] = user.email_usuario
            user_data['senha_usuario'] = user.senha_usuario
            user_data['cnpj'] = user.cnpj
            user_data['create-at'] = user.create_at

            return {'status': 'success', 'message': 'Uma ocorrecia encontradas', 'data': user_data}

    def verify_user(self, senha, email):
        
        user = self.__userDAO.verify_user(senha, email)

        if user == None:
            return {'status': 'error', "message": "Senha ou email incorretos", 'data': {}}
        
        else:
            user_data = {}
            user_data['nome'] = user.nome
            user_data['email_usuario'] = user.email_usuario
            user_data['senha_usuario'] = user.senha_usuario
            return {'status': 'success', "message": "Uma ocorrencia encontrada", 'data': user_data}


        
