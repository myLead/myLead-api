from flask_sqlalchemy import SQLAlchemy
from mylead import db
from dbhelper import Usuario

class UsuarioDAO():

    def create_user(self, user):
        db.session.add(user)
        db.session.commit()

    def get_user(self,email=None, id=None):
        if id == None:
            usuarioexistente = Usuario.query.filter_by(email_usuario = email).first()
            return usuarioexistente
        else:
            usuarioexistente = Usuario.query.filter_by(id_usuario = id).first()
            return usuarioexistente
               
    def delete_user(self, user):
        db.session.delete(user)
        db.session.commit()
        
