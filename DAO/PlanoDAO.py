from flask_sqlalchemy import SQLAlchemy
from mylead import db
from dbhelper import Plano

class PlanoDAO():

    # def create_user(self, user):
    #     db.session.add(user)
    #     db.session.commit()

    def getPlanoById(self, id):

        plano = Plano.query.filter_id(id_plano = id).first()
        return plano

            
