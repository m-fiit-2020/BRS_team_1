import unittest
from Controller import Checker


class TestChecker(unittest.TestCase):
    def test_check_email(self):
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
        for i in list_emails:
            self.assertEqual(Checker.check_email(i), True)
        for j in list_wrong_emails:
            self.assertEqual(Checker.check_email(j), False)

    def test_check_phone(self):
        list_phones = ("+79244669579", "+79969141275", "+79142981921", "+79243601678", "+79142247346", "+79990602363",
                       "+79142334939", "+79244640551", "+79248668556", "89618697027", "89100851951", "89142202681",
                       "89142673402", "89248751088", "89991736337")
        list_wrong_phones = (
        "+79244669579344", "7996914127544", "sas;klfj", "+7924360167!", "+79142247346?", "_79990602363",
        "+89142334939", "+99244640551", 23456656, "896186970277", (8, 9, 2, 4, 4, 6, 6, 9, 5, 7, 9), "&!&lsd?",
        "891426734020", "8924 8751088", "899E1736337")
        for i in list_phones:
            self.assertEqual(Checker.check_phone(i), True)
        for j in list_wrong_phones:
            self.assertEqual(Checker.check_phone(j), False)
