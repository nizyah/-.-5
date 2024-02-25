from abc import ABC, abstractmethod
from typing import List

class Event(ABC):
    """Базовый класс для всех мероприятий."""

    def __init__(self, name: str, location: str, date: str):
        """
        Конструктор класса Event.

        Args:
            name (str): Название мероприятия.
            location (str): Местоположение мероприятия.
            date (str): Дата мероприятия.
        """
        self.name = name
        self.location = location
        self.date = date

    @abstractmethod
    def display_details(self) -> None:
        """Выводит информацию о мероприятии."""
        pass

    def __str__(self) -> str:
        """Строковое представление объекта."""
        return f"{self.name} ({self.date}) at {self.location}"

    def __repr__(self) -> str:
        """Представление объекта."""
        return f"Event(name={self.name}, location={self.location}, date={self.date})"


class Concert(Event):
    """Класс, представляющий концерт."""

    def __init__(self, name: str, location: str, date: str, performers: List[str]):
        """
        Конструктор класса Concert.

        Args:
            name (str): Название концерта.
            location (str): Местоположение концерта.
            date (str): Дата концерта.
            performers (List[str]): Список исполнителей.
        """
        super().__init__(name, location, date)
        self.performers = performers

    def display_details(self) -> None:
        """Выводит подробности о концерте."""
        print(f"Concert: {self.name}")
        print(f"Date: {self.date}")
        print(f"Location: {self.location}")
        print("Performers:")
        for performer in self.performers:
            print(f"- {performer}")

    # Перегрузка метода display_details для концерта, чтобы добавить информацию о исполнителях
    def display_details(self) -> None:
        """
        Выводит подробности о концерте с указанием исполнителей.

        Метод перегружен для добавления информации о списках исполнителей.
        """
        super().display_details()
        print("Performers:")
        for performer in self.performers:
            print(f"- {performer}")


if __name__ == "__main__":
    concert = Concert("RockFest", "Central Park", "2024-05-15", ["Band A", "Band B", "Band C"])
    concert.display_details()
    print(concert)