import re


class Checker:
    """Атрибуты класса: электронная почта, номер телефона."""
    def __init__(self, email: str, phone: str):
        self.email = email
        self.phone = phone

    def check_email(self):
        """Проверяет надпись электронной почты. Пока что знает только 'gmail.com' и 'mail.ru'"""
        if re.match(r'(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)', self.email):
            print("email написан правильно")
            return True
        else:
            print("непрвильно ввели адрес email")
            return False

    def check_phone(self):
        """Проверяет надпись номера телефона"""
        if (self.phone[0:2] == "89" and len(self.phone) == 11) or (self.phone[0:3] == "+79" and len(self.phone) == 12):
            print("номер телефона написали правильно")
            return True
        else:
            print("непрвильно ввели номер телефона")
            return False


