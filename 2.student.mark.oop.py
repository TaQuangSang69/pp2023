students=[]
courses=[]
marks = []
class student:
    def __init__(self, name, id, dob):
        self.__name = name
        self.__id = id
        self.__dob = dob
    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_dob(self):
        return self.__dob
    def set_name(self, name):
        self.__name = name
    def set_id(self, id):
        self.__id = id
    def set_dob(self, dob):
        self.__dob = dob

class course:
    def __init__(self, name, id):
        self.__name = name
        self.__id = id
    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def set_name(self, name):
        self.__name = name
    def set_id(self, id):
        self.__id = id
   
class mark:
    student_ids=[]
    student_marks=[]
    def __init__(self, course):
        self.__course = course
    def get_course(self):
        return self.__course
    def set_course(self, course):
        self.__course = course
    def add_mark(self, id, mark):
        self.student_ids.append(id)
        self.student_marks.append(mark)
    def __str__ (self):
        return str(self.student_ids) + str(self.student_marks)
    
def input_number_students():
    return int(input("Enter number of students: "))
def input_students_info():
    for i in range(input_number_students()):
        id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student dob: ")
        students.append(student(name, id, dob))
def input_number_courses():
    return int(input("Enter number of courses: "))
def input_courses_info():
    for i in range(input_number_courses()):
        id = input("Enter course id: ")
        name = input("Enter course name: ")
        courses.append(course(name, id))

def input_marks():
    choose_course = input("Enter course id: ")
    for i in courses:
        if i.get_id() == choose_course:
            this_mark=mark(choose_course)
    marks.append(this_mark)
    for i in students:
        student_mark = int(input("Enter mark for {}: ".format(i.get_name())))
        student_id = i.get_id()
        this_mark.add_mark(student_id, student_mark)

def list_students():
    for i in students:
        print("Student id: {}, name: {}, dob: {}".format(i.get_id(), i.get_name(), i.get_dob()))
def list_courses():
    for i in courses:
        print("Course id: {}, name: {}".format(i.get_id(), i.get_name()))
def list_marks():
    choose_course = input("Enter course id: ")
    for i in marks:
        a = i.get_course()
        if int(a) == int(choose_course):
            print(i)
            
def main():
    while True:
        print("1. Input students info")
        print("2. Input courses info")
        print("3. Input marks")
        print("4. List students")
        print("5. List courses")
        print("6. List marks")
        print("7. Exit")
        choose = int(input("Choose: "))
        if choose == 1:
            input_students_info()
        elif choose == 2:
            input_courses_info()
        elif choose == 3:
            input_marks()
        elif choose == 4:
            list_students()
        elif choose == 5:
            list_courses()
        elif choose == 6:
            list_marks()
        elif choose == 7:
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()

    
        
    