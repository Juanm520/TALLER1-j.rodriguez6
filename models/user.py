
class User():
    def __init__(self, id, username, password):
        self.__id = id
        self.__username = username
        self.__password = password
    
    @property
    def id(self):
        return self.__id

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username:str) -> str:
        if isinstance(username, str) and username != '':
            self.__username = username

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, nuevo_password:str) -> str:
        if isinstance(nuevo_password, str) and nuevo_password != '':
            self.__password = nuevo_password
            