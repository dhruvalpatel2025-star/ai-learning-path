students = {"Hermione": "Grifindor",
            "Harry": "grifindor",
            "Ron": "Grifindor",
            "Draco": "Slitherin"
            }

# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"])

for student in students:  
    print(student, students[student], sep="- ")