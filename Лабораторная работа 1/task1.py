# TODO: Подробно описать три произвольных класса
import doctest
# TODO: описать класс
class Smartphone:
    """
    >>> smartphone = Smartphone("Huawei", "Pura 70", 512)
    >>> smartphone.install_app("Yandex")
    'установленное приложение: Yandex'
    >>> smartphone.check_storage(56)
    'Достаточно места для хранения'
    >>> smartphone.get_brand_model()
    'Huawei Pura 70'
    """
    def __init__(self, brand: str, model: str, storage: int):
        """
        Создаёт объект смартфона.
        :param brand: Бренд смартфона.
        :param model: Модель телефона.
        :param storage: Объем хранилища смартфона.
        """
        self.brand = brand
        self.model = model
        self.storage = storage

    def get_brand_model(self) -> str:
        """
        Возвращает бренд и модель смартфона.
        """
        return f"{self.brand} {self.model}"

    def install_app(self, app_name: str) -> str:
        """
        Установка приложения на смартфон.
        :param app_name: Название приложения для скачивания.
        :return: Уведомление, сообщающее об установке приложения.
        """
        return f"установленное приложение: {app_name}"

    def check_storage(self, file_size: int) -> str:
        """
        Проверяет, достаточно ли места на телефоне для файла.
        :param file_size: Размер проверяемого файла в гигабайтах.
        :return: Достаточно ли места или нет.
        """
        if file_size < 0:
            raise ValueError("Размер файла должен быть положительным числом")
        if file_size > self.storage:
            return "Недостаточно места для хранения"
        return "Достаточно места для хранения"

# TODO: описать ещё класс
class Laptop:
    """
    >>> laptop = Laptop("Dell", 50)
    >>> laptop.charge(30)
    80
    >>> laptop.power_on()
    >>> laptop.is_on
    True
    >>> laptop.power_off()
    >>> laptop.is_on
    False
    """

    def __init__(self, brand: str, battery_capacity: int):
        """
        Создаёт объект ноутбука.
        :param brand: Бренд ноутбука.
        :param battery_capacity: Ёмкость батареи (в %). Должна быть от 0 до 100.
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой.")
        if not (0 <= battery_capacity <= 100):
            raise ValueError("Ёмкость батареи должна быть в диапазоне от 0 до 100.")

        self.brand = brand
        self.battery_capacity = battery_capacity
        self.is_on = False  # Состояние ноутбука

    def power_on(self) -> None:
        """Включает ноутбук."""
        if self.battery_capacity == 0:
            raise ValueError("Невозможно включить ноутбук: батарея разряжена.")
        self.is_on = True

    def power_off(self) -> None:
        """Выключает ноутбук."""
        self.is_on = False

    def charge(self, amount: int = 10) -> int:
        """
        Заряжает ноутбук.
        :param amount: Процент заряда (по умолчанию 10%). Должен быть положительным.
        :return: Текущий уровень заряда батареи.
        """
        if amount <= 0:
            raise ValueError("Зарядка должна быть положительным числом.")
        self.battery_capacity = min(self.battery_capacity + amount, 100)
        return self.battery_capacity

# TODO: и ещё один
class Book:
    """
    >>> book = Book("Python Basics", 300)
    >>> book.read(50)
    50
    >>> book.progress()
    16.67
    >>> book.read(100)
    150
    >>> book.progress()
    50.0
    """

    def __init__(self, title: str, total_pages: int):
        """
        Создаёт объект книги.
        :param title: Название книги.
        :param total_pages: Общее количество страниц. Должно быть положительным.
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой.")
        if not isinstance(total_pages, int) or total_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")

        self.title = title
        self.total_pages = total_pages
        self.current_page = 0  # Начальная страница

    def read(self, pages: int) -> int:
        """
        Читает заданное количество страниц.
        :param pages: Количество страниц для чтения. Должно быть положительным.
        :return: Текущая страница.
        """
        if pages <= 0:
            raise ValueError("Количество страниц для чтения должно быть положительным.")
        self.current_page = min(self.current_page + pages, self.total_pages)
        return self.current_page

    def progress(self) -> float:
        """
        Возвращает прогресс чтения книги в процентах.
        :return: Прогресс в процентах, округлённый до двух знаков после запятой.
        """
        return round((self.current_page / self.total_pages) * 100, 2)

    if __name__ == "__main__":
        doctest.testmod()
