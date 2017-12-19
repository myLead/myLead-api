from DAO.UsuarioDAO import *

class UsuarioController():

    def __init__(self):
        self.__userDAO = UsuarioDAO()

    #CONECTAR A CRAÇÃO DAS TABELAS PLANO E COMPRA JUNTO 
    #COM A TABELAD DE USUARO
    def create_user(self, user):

        usuarioexistente = self.__userDAO.get_user_by_email(user.email_usuario)

        if usuarioexistente == None:
    
            user = self.__userDAO.create_user(user)
            return user

        else:
            return usuarioexistente

    def delete_user(self, id):

        user = self.__userDAO.get_user_by_id(id)

        if user == None:
            return user
    
        else:
            self.__userDAO.delete_user(user)
            return user

    def list_user(self):

        users = self.__userDAO.list()

        return users


    def list_one_user(self, id):

        user = self.__userDAO.list_one_user(id)   

        return  user

    def verify_user(self, senha, email):
     
        user = self.__userDAO.verify_user(senha, email)
        
        return user

    def getLast(self):
        user = self.__userDAO.getLastUser()
        return user


        
