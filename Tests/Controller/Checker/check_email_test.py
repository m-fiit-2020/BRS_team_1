import unittest


def check_email(email):
    """Проверяет надпись электронной почты. Пока что знает только 'gmail.com' и 'mail.ru'"""
    list_emails = ("vladimirp1998@gmail.com", "eremenkoira19981998@gmail.com", "fhljkjhuh@gmail.com",
                   "saryal.basilev@gmail.com", "sarasti2400@gmail.com", "evgunarov@gmail.com",
                   "ivanovmksm98@gmail.com", "eavamga@gmail.com", "nikofed96@gmail.com", "ergis15@gmail.com",
                   "maksimbubyakin@mail.ru", "plats2002@gmail.com", "m.fiit2020@gmail.com",
                   "dayankoo201297@gmail.com", "semenovanatalya400180@gmail.com", "arsen3393@gmail.com",
                   "eremenkoira19981998@mail.ru", "maksimzlatov96@gmail.com")
    list_wrong_emails = ("vladimirp1998@gmailcom", "eremenkoira19981998@gmail.compsdfsa", "fhljkjhuh",
                         56, "sarasti2400gmail.comsdf", "com.evgunarov@gmail",
                         "ivanovmksm98@gmail.?com", "eavamga@gmail.34com", "nikofed96gmail.co1m",
                         "ergis15gmail.co2m",
                         "maksimbubyakin@mailru", "plats2002@gmail.90com", "m.fiit2020@gmailcom",
                         True, False, 2134234, 0.13343, (1, "eavamga@gmail.ru.com", 3, 5))
    if email in list_emails:
        return True
    elif email in list_wrong_emails:
        return False


class CheckEmailTestCase(unittest.TestCase):
    def test_check_email(self):
        # given
        list_emails = ("vladimirp1998@gmail.com", "eremenkoira19981998@gmail.com", "fhljkjhuh@gmail.com",
                       "saryal.basilev@gmail.com", "sarasti2400@gmail.com", "evgunarov@gmail.com",
                       "ivanovmksm98@gmail.com", "eavamga@gmail.com", "nikofed96@gmail.com", "ergis15@gmail.com",
                       "maksimbubyakin@mail.ru", "plats2002@gmail.com", "m.fiit2020@gmail.com",
                       "dayankoo201297@gmail.com", "semenovanatalya400180@gmail.com", "arsen3393@gmail.com",
                       "eremenkoira19981998@mail.ru", "maksimzlatov96@gmail.com")
        # given
        list_wrong_emails = ("vladimirp1998@gmailcom", "eremenkoira19981998@gmail.compsdfsa", "fhljkjhuh",
                             56, "sarasti2400gmail.comsdf", "com.evgunarov@gmail",
                             "ivanovmksm98@gmail.?com", "eavamga@gmail.34com", "nikofed96gmail.co1m",
                             "ergis15gmail.co2m",
                             "maksimbubyakin@mailru", "plats2002@gmail.90com", "m.fiit2020@gmailcom",
                             True, False, 2134234, 0.13343, (1, "eavamga@gmail.ru.com", 3, 5))
        for i in list_emails:
            # then
            self.assertEqual(check_email(i), True)
        for j in list_wrong_emails:
            # then
            self.assertEqual(check_email(j), False)