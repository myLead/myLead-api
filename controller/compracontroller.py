from DAO.CompraDAO  import *

class CompraController():

    def __init__(self):
        self.__compraDAO = CompraDAO()


    def createComopra(self, compra):

        self.__compraDAO.create_compra(compra)

       

    # def delete_user(self, id):

    #     user = self.__userDAO.get_user_by_id(id)
    #     if user == None:

    #         return user
    #     else:
    #         self.__userDAO.delete_user(user)
    #         return user

    # def list_user(self):

    #     users = self.__userDAO.list()
        
    #     if users == None:
    #         return  users
        
    #     else:

    #         output = []

    #         for user in users:
    #             user_data = {}
    #             user_data['id_usuario'] = user.id_usuario
    #             user_data['nome'] = user.nome
    #             user_data['email_usuario'] = user.email_usuario
    #             user_data['senha_usuario'] = user.senha_usuario
    #             user_data['cnpj'] = user.cnpj
    #             user_data['create_at'] = user.create_at
    #             output.append(user_data)
    #         return  output

    # def list_one_user(self, id):
    #     user = self.__userDAO.list_one_user(id)

    #     if user ==None:
    #         return user
    #     else:

    #         user_data = {}
    #         user_data['id_usuario'] = user.id_usuario
    #         user_data['nome'] = user.nome
    #         user_data['email_usuario'] = user.email_usuario
    #         user_data['senha_usuario'] = user.senha_usuario
    #         user_data['cnpj'] = user.cnpj
    #         user_data['create-at'] = user.create_at

    #         return  user_data

    # def verify_user(self, senha, email):
        
    #     user = self.__userDAO.verify_user(senha, email)

    #     if user == None:
    #         return user
        
    #     else:
    #         user_data = {}
    #         user_data['id_usuario'] = user.id_usuario
    #         user_data['email_usuario'] = user.email_usuario
    #         return user_data


        
