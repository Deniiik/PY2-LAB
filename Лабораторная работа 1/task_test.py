
# TODO: импортируйте классы, созданные в ходе выполнения прошлого задания
from task_1 import Smartphone, Laptop, Book


if __name__ == "__main__":
    smartphone = Smartphone("Huawei", "Pura 70", 512)
    book = Book("Hobbit", 200)
    laptop = Laptop("Honor", 40)

    try:
        book.read(-5)
    except ValueError:
        print(f"Ошибка: неправильные данные")

    try:
        laptop.charge(-8)
    except ValueError:
        print(f"Ошибка: неправильные данные")

    try:
        smartphone.check_storage(-5)
    except ValueError:
        print(f"Ошибка: неправильные данные")
