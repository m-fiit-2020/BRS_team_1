def check_email(email: str):
    """Проверяет надпись электронной почты. Пока что знает только 'gmail.com' и 'mail.ru'"""
    list_emails = ("vladimirp1998@gmail.com", "eremenkoira19981998@gmail.com", "fhljkjhuh@gmail.com",
                   "saryal.basilev@gmail.com", "sarasti2400@gmail.com", "evgunarov@gmail.com",
                   "ivanovmksm98@gmail.com", "eavamga@gmail.com", "nikofed96@gmail.com", "ergis15@gmail.com",
                   "maksimbubyakin@mail.ru", "plats2002@gmail.com", "m.fiit2020@gmail.com",
                   "dayankoo201297@gmail.com", "semenovanatalya400180@gmail.com", "arsen3393@gmail.com",
                   "eremenkoira19981998@mail.ru", "maksimzlatov96@gmail.com")
    if email in list_emails:
        return True
    return False


def check_phone(phone: str):
    """Проверяет надпись номера телефона"""
    list_phones = ("+79244669579", "+79969141275", "+79142981921", "+79243601678", "+79142247346", "+79990602363",
                   "+79142334939", "+79244640551", "+79248668556", "89618697027", "89100851951", "89142202681",
                   "89142673402", "89248751088", "89991736337")
    if phone in list_phones:
        return True
    return False


def check_brs_points(point: int):
    """Проверяет количество баллов"""
    list_points = (
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
        21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
        39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
        57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74,
        75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92,
        93, 94, 95, 96, 97, 98, 99, 100)
    if point in list_points:
        return True
    return False
