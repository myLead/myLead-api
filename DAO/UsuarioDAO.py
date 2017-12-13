from flask_sqlalchemy import SQLAlchemy
from mylead import db
from dbhelp import Usuario

class UsuarioDAO():

    def create_user(self, user):
        db.session.add(user)
        db.session.commit()

    def get_user(self,email):
        usuarioexistente = Usuario.query.filter_by(
            email_usuario=email).first()
        return usuarioexistente
   
    # def delete_user(self, user):
        
