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


def check_email(email: str):
    """Проверяет надпись электронной почты."""
    if re.match(r'(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)', email):
        print("email написан правильно")
        return True
    else:
        print("непрвильно ввели адрес email")
        return False


def check_phone(phone: str):
    """Проверяет надпись номера телефона"""
    if (phone[0:2] == "89" and len(phone) == 11) or (phone[0:3] == "+79" and len(phone) == 12):
        print("номер телефона написали правильно")
        return True
    else:
        print("непрвильно ввели номер телефона")
        return False