from DAO.PlanoDAO import *

class PlanoController():

    def __init__(self):

        self.__planoDAO = PlanoDAO()


    def getPlano(self, id_plano):
        
        plano = self.__planoDAO.getPlanoById(id_plano)

        if plano == None:
            return {'status': 'error', "message": "Plano inexistente", 'data': {}}
        
        else:
            plano_data                    = {}
            plano_data['descricao_plano'] = plano.descricao_plano
            plano_data['valor']           = plano.valor
            plano_data['id_plano']        = plano.id_plano

            return {'status': 'success', "message": "Usuário encontrado com sucesso", 'data': plano_data}


        
