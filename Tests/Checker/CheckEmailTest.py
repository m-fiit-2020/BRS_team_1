import unittest
from Tests.Mock.Checker import check_email
import Checker


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

        for email in list_emails:
            # when
            is_email = check_email(email)
            # then
            self.assertEqual(is_email, True)
        for wrong_email in list_wrong_emails:
            # when
            is_email = check_email(wrong_email)
            # then
            self.assertEqual(is_email, False)
        # after TDD
        for email in list_emails:
            # when
            is_email = check_email(email)
            developed_is_email = Checker.check_email(email)
            # then
            self.assertEqual(is_email, developed_is_email)
        for wrong_email in list_wrong_emails:
            # when
            is_email = check_email(email)
            developed_is_email = Checker.check_email(email)
            # then
            self.assertEqual(is_email, developed_is_email)
