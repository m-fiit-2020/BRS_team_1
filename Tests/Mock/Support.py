from Model.Group import Group
from Model.Subject import Subject


def equalGroups(groups1: [Group], groups2: [Group]):
    if len(groups1) != len(groups2):
        return False
    for i in range(len(groups1)):
        if groups1[i].name != groups2[i].name and groups1[i].year != groups2[i].year:
            return False
    return True


def equalSubjects(subject1: [Subject], subject2: [Subject]):
    if len(subject1) != len(subject2):
        return False
    for i in range(len(subject1)):
        if subject1[i].code != subject2[i].code and subject1[i].name != subject2[i].name:
            return False
    return True
