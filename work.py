text = "LA"
number = 5
student_name = ["Mark", "Hans", "Kasper", "Jonas"]

if number == 10:
    print("Det er 10")
else:
    if number == 5 and text == "Hello":
        print("Det er " + str(number))
    else:
        print("Der er en fejl pt...")
        
        
print(student_name)
print(len(student_name))

student_name[1] = "Louise"
student_name.append("Sofie") #tilføj til listen
student_name.append("Mette") #tilføj til listen

print(student_name)
print(len(student_name))

#Fjern nr "4" fra listen
#del student_name[3]
#print(student_name)

for name in student_name:
    print("Studie navne: {0}".format(name))

x = 0

for index in range(10):
    x += 1
    print("Value er {0}".format(x))