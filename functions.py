students = []

def getStudents():
    student_TitleCase = []
    for student in students:
        student_TitleCase.append(student["name"].title())
    return student_TitleCase

def printStudent():
    student_TitleCase = getStudents()
    print(student_TitleCase)
    
def addStudent(name, area):
    student = {"name": name, "area":area }
    students.append(student)

def saveFile(student):
    try:
        f = open("student.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save file")

def readFile():
    try:
        f = open("student.txt", "r")
        for student in f.readlines():
            addStudent(student)
        f.close()
    except Exception:
        print("Could not read file")

readFile()
printStudent()

studentName = input("skriv student navn: ")
studentArea = input("skriv området til student: ")

addStudent(studentName, studentArea)
saveFile(studentName)
