from flask_sqlalchemy import SQLAlchemy
from mylead import db
from dbhelper import *

class CsvDAO():
    def createBaseCsv(self, file):
        db.session.add(file)
        db.session.commit()

    def getBaseCsv(self, id_usuario):
        data = CsvFile.query.filter_by(id_usuario=id_usuario).first()
        return data
        
