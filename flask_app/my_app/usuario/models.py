from my_app import db
 
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Usuario(db.Model):
    
    
    id = db.Column(db.INT(), primary_key=True)
    nome_usuario = db.Column(db.VARCHAR(100), nullable=True)
    email_usuario = db.Column(db.VARCHAR(150), nullable=True)
    senha_usuario = db.Column(db.VARCHAR(32), nullable=True)

    def __init__(self, nome_usuario, email_usuario, senha_usuario):
        self.nome_usuario = nome_usuario
        self.email_usuario = email_usuario
        self.senha_usuario = senha_usuario

# class TabelaPlano(db.Model):

#     __tablename__ = 'Plano'

#     id = db.Column(db.INT(), primary_key = True)
#     descricao_plano = db.Column(db.VARCHAR(150), nullable = True)
#     valor_plano = db.Column( db.FLOAT(), nullable = False)

#     def __init__(self, id_plano, descricao_plano, valor_plano):
#         self.id_plano = id_plano
#         self.descricao_plano = descricao_plano
#         self.valor_plano =valor_plano

# class TabelaCompra(db.Model):

#     __tablename__ = 'Compra'

#     id = db.Column(db.INT(), primary_key = True)
#     id_usuario = db.Column(db.INT(), ForeignKey(usuario.id), nullable = False)
#     id_plano = db.Column(db.INT(), ForeignKey(Plano.id), nullable=False)
#     data_compra = Column(db.DATE(), nullable = False)
#     data_vencimento = Column(db.DATE(), nullable = False)

#     def __init__(self, id, id_usuario, id_plano, data_compra, data_vencimento):
#         self.id = id
#         self.id_usuario = id_usuario
#         self.id_plano = id_plano
#         self.data_compra = data_compra
#         self.data_vencimento = data_vencimento