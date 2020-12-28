import unittest
from Controller import Checker


class CheckPhoneTestCase(unittest.TestCase):
    def test_check_phone(self):
        list_phones = ("+79244669579", "+79969141275", "+79142981921", "+79243601678", "+79142247346", "+79990602363",
                       "+79142334939", "+79244640551", "+79248668556", "89618697027", "89100851951", "89142202681",
                       "89142673402", "89248751088", "89991736337")
        list_wrong_phones = ("+79244669579344", "7996914127544", "sas;klfj", "+7924360167!", "+79142247346?",
                             "_79990602363", "+89142334939", "+99244640551", 23456656, "896186970277",
                             (8, 9, 2, 4, 4, 6, 6, 9, 5, 7, 9), "&!&lsd?", "891426734020", "8924 8751088",
                             "899E1736337")
        for i in list_phones:
            self.assertEqual(Checker.check_phone(i), True)
        for j in list_wrong_phones:
            self.assertEqual(Checker.check_phone(j), False)
