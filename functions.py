students = []

def getStudents():
    student_TitleCase = []
    for student in students:
        student_titleCase = student.title()
    return student_titleCase

def printStudent():
    student_TitleCase = getStudents()
    print(student_TitleCase)
    
def addStudent(name, studentId):
    student = {"name": name, "studentId":studentId }
    students.append(student)

addStudent("Jesper Petersen", 22511)
