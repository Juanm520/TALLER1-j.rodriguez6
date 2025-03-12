import uuid
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, username, password, nombre, is_admin):
        self.__id = uuid.uuid4()
        self.__username = username
        self.__password = password
        self.__nombre = nombre
        self.__is_admin = is_admin
    
    @property
    def id(self):
        return self.__id
    
    @property
    def nombre(self):
        return self.__nombre

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

    @property
    def is_admin(self):
        return self.__is_admin
    @is_admin.setter
    def is_admin(self, nuevo_is_admin:bool) -> bool:
        if isinstance(nuevo_is_admin, bool) and nuevo_is_admin != '':
            self.__is_admin = nuevo_is_admin

users = {
    'antonitor' : User('antonitor', 'Tonito123', 'Antonio Restrepo', False),
    'pacoV32' : User('pacoV32', 'ElPaquitoV3232', 'Paco Villareal', False),
    'quintano_el_real': User('quintano_el_real', 'quintanoPro98', 'Quintano Real', False),
    'mengano_cruz' : User('mengano_cruz', 'C284y9)Pgb3P', 'Anatolio Mengano Cruz Cespedes', True)
    }