"""Importacion del modulo de JSON"""

from datetime import datetime

# import json
import files


def save_log(func):
    """Decorador de guardado de Logs"""

    def wrapper(self):
        func(self)
        file_name = "activity.log"
        today = str(datetime.today())
        content = f"{today} => {type(self).__name__} saved successfully\n"

        try:
            files.read(file_name)
        except FileNotFoundError:
            files.create(file_name)

        files.update2(file_name, content)
        print(content)

    return wrapper


def save_data(file_name, data):
    """Function to save data"""
    try:
        files.read(file_name)
    except FileNotFoundError:
        files.create(file_name, data)
        return data
    files.update2(file_name, data)
    return data


class User:
    """Definición de la Clase User"""

    def __init__(self, first_name, last_name, user_name, email, password, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.email = email
        self.password = password
        self.age = age

    def as_dict(self):
        """Definición del Método as_dict para formateo de la información como directorio"""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "user_name": self.user_name,
            "email": self.email,
            "password": self.password,
            "age": self.age,
        }

    def raise_age(self):
        """Definición del Método raise age para aumentar la edad en una unidad"""
        self.age += 1
        return self.age

    @save_log
    def save(self):
        """Definición del Método de save para guardar nueva data dentro del archivo users.json"""

        file_name = "users.json"
        return save_data(file_name, self.__dict__)


class Article:
    """Definición de la Clase Article"""

    def __init__(self, title, content, status, image, created_by) -> None:
        self.title = title
        self.content = content
        self.status = status
        self.image = image
        self.created_by = created_by

    def as_dict(self):
        """Definición del Método as_dict para formateo de la información como directorio"""
        return {
            "title": self.title,
            "content": self.content,
            "status": self.status,
            "image": self.image,
            "created_by": self.created_by,
        }

    @save_log
    def save(self):
        """Definición del Método de save para guardar nueva data dentro del archivo articles.json"""

        file_name = "articles.json"
        return save_data(file_name, self.__dict__)


class Comment:
    """Definición de la Clase Comments"""

    def __init__(self, content, article, created_by) -> None:
        self.content = content
        self.article = article
        self.created_by = created_by

    def as_dict(self):
        """Definición del Método as_dict para formateo de la información como directorio"""
        return {
            "content": self.content,
            "article": self.article,
            "created_by": self.created_by,
        }

    @save_log
    def save(self):
        """Definición del Método de save para guardar nueva data dentro del archivo comments.json"""

        file_name = "comments.json"
        return save_data(file_name, self.__dict__)


user1 = User("Ricardo", "Gomez", "Richard7", "ricardo@gmail.com", "password2", 25)
user1.save()

# article1 = Article(
#     "Sidartha", "Un gran libro", "on", "https://image2.com", "Herman Hesse"
# )
# article1.save()

# comment1 = Comment("Maravilloso", "Sidartha", "Peter Parker")
# comment1.save()
