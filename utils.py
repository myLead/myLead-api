from datetime import date

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
