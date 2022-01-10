from collections import defaultdict

class School:
    def __init__(self):
        self.sdb = defaultdict(list)
        self.__added = []

    def add_student(self, name, grade):
        if name not in self.roster():
            self.sdb[grade] += [name]
            self.__added.append(True)
        else:
            self.__added.append(False)            

    def added(self):
        return self.__added

    def roster(self):
        grades = sorted(self.sdb.keys())
        return [student for grade in grades for student in self.grade(grade)]

    def grade(self, grade_number):
        return sorted(self.sdb[grade_number])
