import unittest
from Models.CrossSection import CrossSection


class CrossSectionTestCase(unittest.TestCase):
    def setUp(self):
        self.first_section_expected = 'Первый контрольный срез'
        self.second_section_expected = 'Второй контрольный срез'
        self.final_section_expected = 'Заключительный контрольный срез'

    def test_cross_section(self):
        self.assertEqual(CrossSection.FirstSection.value, self.first_section_expected)
        self.assertEqual(CrossSection.SecondSection.value, self.second_section_expected)
        self.assertEqual(CrossSection.FinalSection.value, self.final_section_expected)


if __name__ == '__main__':
    unittest.main()
