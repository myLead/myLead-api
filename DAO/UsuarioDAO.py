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

    def list(self):
                
        users = Usuario.query.all()
        output = []

        for user in users:
            user_data = {}
            user_data['id_usuario'] = user.id_usuario
            user_data['nome'] = user.nome
            user_data['email_usuario'] = user.email_usuario
            user_data['senha_usuario'] = user.senha_usuario
            user_data['cnpj'] = user.cnpj
            user_data['create_at'] = user.create_at
            output.append(user_data)

        return output

    def list_one_user(self, id):
        
        user = Usuario.query.filter_by(id_usuario = id).first()

        user_data = {}
        user_data['id_usuario'] = user.id_usuario
        user_data['nome'] = user.nome
        user_data['email_usuario'] = user.email_usuario
        user_data['senha_usuario'] = user.senha_usuario
        user_data['cnpj'] = user.cnpj
        user_data['create-at'] = user.create_at

        return user_data

    def verify_user(self, senha, email):
        
        user = Usuario.query.filter_by(senha_usuario = senha, email_usuario = email).first()

        if not user:
            return "error"
        
        user_data = {}
        user_data['nome'] = user.nome
        user_data['email_usuario'] = user.email_usuario
        user_data['senha_usuario'] = user.senha_usuario
        
        return user_data

            
