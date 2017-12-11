class UserDominio():
    def __init__(self, id, public_id, name, password, admin):
        self.__id = id
        self.__public_id = public_id
        self.__name = name
        self.__password = password
        self.__admin = admin

    def getId(self):
        return self._id
    def setId(self, id):
        self._id = id
    def getPublicId(self):
        return self.__public_id
    def setPublicId(self, public_id):
        self.__public_id = public_id
    def getName(self):
        return self.__name
    def setName(self, name):
        self.__name = name
    def getPassword(self):
        return self.__password
    def setPassword(self, password):
        self.__password = password
    def getAdmin(self):
        return self.__admin
    def setAdmin(self, admin):
        self.__admin = admin
    
