import re
from Models.Student import Student


def check_points(student: Student):
    is_true = True
    for points in student.brs_points:
        if points.points > 100:
            print("Балл поставлен НЕКОРРЕКТНО:\n"
                  f"Название предмета: {points.subject.name}\n"
                  f"Код предмета: {points.subject.code}\n"
                  f"Года обучения: c {points.year.begin_year} по {points.year.end_year}\n"
                  f"Срез: {points.cross_section.value}\n"
                  f"Количество баллов: {points.points}")
            is_true = False
    if is_true:
        print("Баллы поставлены правильно")
        return True
    return False


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
