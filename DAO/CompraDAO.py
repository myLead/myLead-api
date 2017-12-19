from flask_sqlalchemy import SQLAlchemy
from mylead import db
from dbhelper import Usuario

class CompraDAO():

    def create_user(self, user, plano):
        db.session.add(user)
        db.session.commit()
