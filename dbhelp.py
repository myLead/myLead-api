from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from mylead import db



class Usuario(db.Model):
    __tablename__ = 'Usuario'
    id_usuario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable = False)
    email_usuario = db.Column(db.String(100), nullable = False)
    senha_usuario = db.Column(db.String(80), nullable = False)
    cnpj = db.Column(db.String(20))
    create_at = db.Column(db.DateTime(), index=True, default=datetime.now)
    

class Compra(db.Model):
    __tablename__ = 'Compra'
    id_compra = db.Column(db.Integer, primary_key=True)
    data_compra = db.Column(db.DateTime(), index=True, default=datetime.now)
    data_vencimento = db.Column(db.Date())
    id_usuario = db.Column(db.INT(), ForeignKey('Usuario.id_usuario'), nullable=False)
    id_plano = db.Column(db.INT(), ForeignKey('Plano.id_plano'), nullable=False)

class Plano(db.Model):
    __tablename__ = 'Plano'
    id_plano  = db.Column(db.Integer, primary_key=True)
    descricao_plano = db.Column(db.TEXT())
    valor = db.Column(db.TEXT())

