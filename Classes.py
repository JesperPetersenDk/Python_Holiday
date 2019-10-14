students = []

class StudentClass:
    def addStudent(self, name, area="Ukendt"):
        student = {"name": name, "area":area }
        students.append(student)

Student = StudentClass()
Student.addStudent("Jesper")

print(students)