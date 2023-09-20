from json import dumps, loads
import time


class UserRepository:
    _userConnection = ""

    def __init__(self, fileName):
        self.fileName = fileName

    def getUsers(self):
        self.__openFileForRead()
        userData = self._userConnection.read()
        if (userData):
            userData = loads(userData)
        else:
            userData = []

        return userData

    def createUser(self, userData):
        self.__openFileForRead()
        allUsers = self.getUsers()

        allUsers.append(userData)
        convertedUserData = dumps(allUsers, indent=4)
        self.__openFileForWrite()
        self._userConnection.write(convertedUserData)

    def deleteById(self, id):
        self.__openFileForRead()
        allUserss = self._userConnection.read()
        allUserss = loads(allUserss)
        for item in range(len(allUserss)):
            if allUserss(item["id"]) == id:
                del item
                break


    def getById(self, id):
        pass

    def __openFileForWrite(self):
        if (self._userConnection):
            self._userConnection.close()
        self._userConnection = open(self.fileName, "w")

    def __openFileForRead(self):
        if (self._userConnection):
            self._userConnection.close()
        self._userConnection = open(self.fileName, "r")


obj = UserRepository("users")
obj.deleteById(1234)
start_time = time.time()
print(obj.getUsers())
end_time = time.time()

print(end_time - start_time)

# obj.createUser(
#     {
#         "name": "Abdulaziz",
#         "age" : 19
#     }
# )