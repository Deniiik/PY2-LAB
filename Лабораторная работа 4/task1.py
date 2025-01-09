# TODO: описать базовый класс
class Animal:
    """
    Базовый класс Animal (Животное).
    Атрибуты:
        name (str): Имя животного.
        age (int): Возраст животного.
        species (str): Вид животного.
    Методы:
        init: Конструктор для инициализации объекта.
        str: Возвращает строковое представление объекта.
        repr: Возвращает строку для внутреннего представления объекта.
        make_sound: Базовый метод для издания звука.
    """

    def __init__(self, name: str, age: int, species: str) -> None:
        self.name = name
        self.age = age
        self.species = species

    def __str__(self) -> str:
        return f"{self.name} is a {self.age}-year-old {self.species}."

    def __repr__(self) -> str:
        return f"Animal(name='{self.name}', age={self.age}, species='{self.species}')"

    def make_sound(self) -> str:
        """
        Метод, который возвращает базовый звук животного.
        """
        return "Some generic animal sound"

# TODO: описать дочерний класс


class Dog(Animal):
    """
    Дочерний класс Dog, наследующий Animal.
    Атрибуты:
        name (str): Имя собаки.
        age (int): Возраст собаки.
        species (str): Вид животного (устанавливается автоматически как "dog").
        breed (str): Порода собаки.
    Методы:
        init: Расширяет конструктор базового класса.
        str: Перегружает строковое представление.
        make_sound: Перегружает метод для издания звука.
    """

    def __init__(self, name: str, age: int, breed: str) -> None:
        """
        Конструктор класса Dog.
        Расширяет базовый класс Animal, добавляя атрибут породы.
        """
        super().__init__(name, age, "dog")
        self.breed = breed

    def __str__(self) -> str:
        return f"{self.name} is a {self.age}-year-old {self.breed} dog."

    def make_sound(self) -> str:
        """
        Перегрузка метода make_sound.
        Собака издает характерный звук, что отличает её от других животных.
        """
        return "Woof! Woof!"


# Пример использования:
if __name__ == "__main__":
    generic_animal = Animal(name="GenericAnimal", age=5, species="unknown")
    dog = Dog(name="Buddy", age=3, breed="Golden Retriever")

    print(generic_animal)
    print(dog)
    print(dog.make_sound())
