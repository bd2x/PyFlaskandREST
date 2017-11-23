class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.grades = []


    def gradeTotal(self):
        return sum(self.grades)

anna = Student("Anna", "UM")
anna.grades.append(39)
anna.grades.append(40)

#print("\n")

print("{}'s total score is {}".format(anna.name, anna.gradeTotal()))

