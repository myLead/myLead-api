from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from mylead import db
from dbhelper import *

class UsuarioDAO():

    def create_user(self, user):
        db.session.add(user)
        db.session.commit()

    def get_user_by_email(self, email):

        user = Usuario.query.filter_by(email_usuario = email).first()
        return user

    def get_user_by_id(self, id):

        user = Usuario.query.filter_by(id_usuario = id).first()
        return user

                       
    def delete_user(self, user):
        db.session.delete(user)
        db.session.commit()

    def list(self):
                
        users = Usuario.query.all()
        return users

    def list_one_user(self, id):
        
        user = Usuario.query.filter_by(id_usuario = id).first()

        return user

    def verify_user(self, senha, email):
        
        user = Usuario.query.filter_by(senha_usuario = senha, email_usuario = email).first()
        
        return user

    def getLastUser(self):

        user = Usuario.query.order_by(desc(Usuario.id_usuario)).first()
        return user.id_usuario       


            
