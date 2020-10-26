import sqlalchemy
from CrossSection import CrossSection
from EducationYear import EducationYear

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(CrossSection.FirstSection.value)
    education_year = EducationYear(begin_year=2020, end_year=2022)
    print(education_year.end_year, education_year.begin_year)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
