from flask_sqlalchemy import SQLAlchemy
from mylead import db
from dbhelper import *

class CompraDAO():
   
    def create_compra(self, compra):
        db.session.add(compra)
        db.session.commit()
