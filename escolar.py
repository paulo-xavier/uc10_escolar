number_students = int(input("Input the students number: ")) 

students = []
genders = []


for i in range(number_students):

    name_student = input(f"Input the student name: ")
    gender_student = input(f"Input the student gender (M/F)").upper()

    grades = []

    for n in range(4):
        grade = float(input(f"Enter the grade {n + 1} from {name_student}"))

        grades.append(grade)

        grades.append({
            
            "name" : name_student, 
            "grades" : grades, 
            "gender" : gender_student
            
            })
        

    print(f"Students number: {i}")
    print(f"Name: {name_student}")
    print(f"Gender: {gender_student}")

    genders.append(gender_student)


# Calculate the average 

averages = []
gender_average = {"M" : [], "F": []}

for student in students:

    name = student["name_student"]
    grades = student["grades"]
    gender = student["gender_student"]

    average = sum(grades) / len(grades)
    averages.append(average)

    gender_average[gender].append(average)

    print(f"Students number: {i}")
    print(f"Name {name}")
    print(f"Gender: {gender}")





# ./env/