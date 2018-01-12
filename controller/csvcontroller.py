from DAO.csvDAO import *

class CsVController():
    def __init__(self):
        self.__csvDao = CsvDAO()

    def createBaseCsv(self, file):
        basecsv = self.__csvDao.createBaseCsv(file)

   
