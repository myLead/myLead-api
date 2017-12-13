from DAO.UsuarioDAO import *

class UsuarioController():

    def __init__(self):
        self.__userDAO = UsuarioDAO()

    
    def create_user(self,user):
        usuarioexistente = self.__userDAO.get_user(user.email_usuario)

        if not usuarioexistente:
            self.__userDAO.create_user(user)
            return 'Usuario criado'
        else:
            return "Usuario já existente"