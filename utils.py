from datetime import date
import csv
import json

class Utils():

    def getDateToday(self):
        today = date.today()
        return today


    def getDateFuture(self):
        today = self.getDateToday()
        futuro = date.fromordinal(today.toordinal() + 120)
        return futuro


    def getDateDiff(self):
        diff = self.getDateFuture() - self.getDateToday()
        return diff

    def csvToJson2(self, file):
        csvfile = open(file, 'r', encoding='utf-8')
        reader = csv.DictReader(csvfile)

        lista = []
        for row in reader:
            x = (json.dumps(row, indent=4, ensure_ascii=False))
            lista.append(x)
        return (', '.join(lista))
    
    def csvToJson(self, file):
        reader = csv.DictReader(file)

        lista = []
        for row in reader:
            x = (json.dumps(row, indent=4, ensure_ascii=False))
            lista.append(x)
        return (', '.join(lista))
