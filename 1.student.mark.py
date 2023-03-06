students = []
courses = []
marks = []

def inputNumberOfStudents():
    return int(input("Enter number of students: "))

def inputStudentsInfo():
    id = input("Enter student id: ")
    name = input("Enter student name: ")
    dob = input("Enter student dob: ")
    return {"id": id, "name": name, "dob": dob}

def inputNumberOfCourses():
    return int(input("Enter number of courses: "))

def inputCoursesInfo():
    id = input("Enter course id: ")
    name = input("Enter course name: ")
    credit = input("Enter course credit: ")
    return {"id": id, "name": name, "credit": credit}

def ListOfStudents(students):
    for student in students:
        print(f"+) {student['name']}")

def ListOfCourses(courses):
    for course in courses:
        print(f"+) {course['name']}")

def inputMark(course, students):
    for student in students:
        mark = input(f"Enter mark of {student['name']} in {course['name']}: ")
        course['mark'][student['id']] = mark

def CourseMarks(course):
    for (student_id, mark) in course['mark'].items():
        print(f"+) {student_id} : {mark}")

number_students = inputNumberOfStudents()
for i in range(number_students):
    students += [inputStudentsInfo()]

number_courses = inputNumberOfCourses()
for i in range(number_courses):
    courses += [inputCoursesInfo()]

for course in courses:
    course['mark'] = {}
    inputMark(course, students)

print("List of students:")
ListOfStudents(students)

print("List of courses:")
ListOfCourses(courses)

print("List of marks:")
for course in courses:
    print(f"{course['name']}:")
    CourseMarks(course)





