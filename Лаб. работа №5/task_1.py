# TODO Написать 3 класса с документацией и аннотацией типов

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
from abc import ABC, abstractmethod

class PhysicalObject(ABC):
    """
    Абстрактный класс для описания материальных объектов.
    """
    def __init__(self, material: str, weight: float):
        """
        Конструктор класса.

        :param material: Материал объекта.
        :type material: str
        :param weight: Вес объекта в килограммах.
        :type weight: float
        """
        self.material = material
        self.weight = weight

    @abstractmethod
    def move(self, destination: str) -> str:
        """
        Метод, описывающий перемещение объекта.

        :param destination: Место, куда перемещается объект.
        :type destination: str
        :return: Сообщение о перемещении объекта.
        :rtype: str
        """
        ...

    @abstractmethod
    def break_down(self) -> str:
        """
        Метод, описывающий поломку объекта.

        :return: Сообщение о поломке объекта.
        :rtype: str
        """
        ...


class AbstractTree(ABC):
    """
    Абстрактный класс для описания деревьев.
    """
    def __init__(self, height: float, age: int):
        """
        Конструктор класса.

        :param height: Высота дерева в метрах.
        :type height: float
        :param age: Возраст дерева в годах.
        :type age: int
        """
        self.height = height
        self.age = age

    @abstractmethod
    def photosynthesis(self, sunlight: int) -> str:
        """
        Метод, описывающий фотосинтез дерева.

        :param sunlight: Интенсивность солнечного света.
        :type sunlight: int
        :return: Сообщение о фотосинтезе дерева.
        :rtype: str
        """
        ...

    @abstractmethod
    def shed_leaves(self) -> str:
        """
        Метод, описывающий опадение листьев дерева.

        :return: Сообщение об опадении листьев.
        :rtype: str
        """
        ...


class AbstractSocialMedia(ABC):
    """
    Абстрактный класс для описания социальных сетей.
    """
    def __init__(self, users: int, platform: str):
        """
        Конструктор класса.

        :param users: Количество пользователей в социальной сети.
        :type users: int
        :param platform: Платформа социальной сети (например, "Facebook").
        :type platform: str
        """
        self.users = users
        self.platform = platform

    @abstractmethod
    def post_message(self, message: str) -> str:
        """
        Метод, описывающий публикацию сообщения в социальной сети.

        :param message: Текст сообщения.
        :type message: str
        :return: Сообщение о публикации.
        :rtype: str
        """
        ...

    @abstractmethod
    def add_friend(self, friend_name: str) -> str:
        """
        Метод, описывающий добавление друга в социальной сети.

        :param friend_name: Имя друга.
        :type friend_name: str
        :return: Сообщение о добавлении друга.
        :rtype: str
        """
        ...
