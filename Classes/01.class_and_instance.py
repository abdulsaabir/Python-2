class Student:
    # class constructor
    def __init__(self, name, age, classroom):
        self.name = name
        self.age = age
        self.classroom = classroom

        self.attendance_count = 0
        self.courses_enrolled = []

    def set_attendance(self):
        self.attendance_count += 1

    def add_course(self, course):
        self.courses_enrolled.append(course)

    def get_attendance_count(self):
        return self.attendance_count

    def get_courses_enrolled(self):
        return self.courses_enrolled

# Creating instances of the Student 

# student 1 object
student1 = Student("Ahned Wehliye", 18, "B6")
student1.set_attendance()
student1.set_attendance()
student1.set_attendance()
student1.add_course("PHP")
student1.add_course("Discrete Math")


# print student 1 object properties
print('----------- student 1----------------')
print('student 1 name is: ', student1.name)
print('student 1 age: ', student1.age)
print('student 1 classroom: ', student1.classroom)
print('Student 1 has attended : ', student1.get_attendance_count(),  'days')
print('student 1 enrolled ', student1.courses_enrolled, 'courses')



# student 2 object
student2 = Student("Saabiriin Faarax", 19, "B7")
student2.add_course("python-2")


# print student 2 object properties
print('----------- student 2----------------')
print('student 2 name is: ', student2.name)
print('student 2 age: ', student2.age)
print('student 2 classroom: ', student2.classroom)
print('Student 2 has attended : ', student2.get_attendance_count(),  'days')
print('student 2 enrolled ', student2.courses_enrolled, 'courses')

# student 3 object
student3 = Student("Siciid abdulkhaadir", 17, "B4")
student3.set_attendance()
student3.add_course("JS")
student3.add_course("HTML")
student3.add_course("Data Structures")


# print student 2 object properties
print('----------- student 3----------------')
print('student 3 name is: ', student3.name)
print('student 3 age: ', student3.age)
print('student 3 classroom: ', student3.classroom)
print('Student 3 has attended : ', student3.get_attendance_count(),  'days')
print('student 3 enrolled ', student3.courses_enrolled, 'courses')