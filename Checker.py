import re

class Checker:
    """Атрибуты класса: электронная почта, номер телефона."""
    def __init__(self, email: str, phone: str):
        self.email = email
        self.phone = phone

    def check_email(self):
        """Проверяет надпись электронной почты. Пока что знает только 'gmail.com' и 'mail.ru'"""
        if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-z.]{2,6}$)", str(self.email)):
            print("правильный email")
            return True
        else:
            print("непрвильный email")
            return False


    def check_phone(self):
        """Проверяет надпись номера телефона"""
        if re.match(r"(^(\+7)|8)\d{10}$", str(self.phone)):
            print("правильный номер")
            return True
        else:
            print("неправильный номер")
            return False

    def check_points(self):
