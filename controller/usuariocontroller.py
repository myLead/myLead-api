from DAO.UsuarioDAO import *

class UsuarioController():

    def __init__(self):
        self.__userDAO = UsuarioDAO()

    
    def create_user(self, user):
        usuarioexistente = self.__userDAO.get_user(user.email_usuario)

        if not usuarioexistente:
            self.__userDAO.create_user(user)
            return {'status': 'success', 'message': 'Usuario cadastrado', 'data': {}}
        else:
            return {'status': 'error', 'message': 'Email ja cadastrado', 'data': {}}
    def delete_user(self, id):
        usuarioexistente = self.__userDAO.get_user(id=id)

        if not usuarioexistente:
            return {'status': 'error', 'message': 'Usuario nao encontrado', 'data': {}}
        else:
            self.__userDAO.delete_user(usuarioexistente)
            return {'status': 'sussecc', 'message': 'Usuario deletado', 'data': {}}
