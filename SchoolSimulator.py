class Student:
    def __init__(self, name, grade_level):
        self.name = name
        self.grade_level = grade_level
        self.courses = []
        
    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)
            course.add_student(self)
            
    def drop_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            course.remove_student(self)
            
    def __repr__(self):
        return f"{self.name} ({self.grade_level})"

class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students = []
        
    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            student.add_course(self)
            
    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            student.drop_course(self)
            
    def __repr__(self):
        return f"{self.name} ({self.teacher})"

# Create some instances of the Student class
alice = Student("Alice", 9)
bob = Student("Bob", 10)
charlie = Student("Charlie", 11)

# Create some instances of the Course class
math = Course("Math", "Ms. Smith")
english = Course("English", "Mr. Johnson")
science = Course("Science", "Mrs. Lee")

# Add students to courses
math.add_student(alice)
math.add_student(bob)
english.add_student(bob)
english.add_student(charlie)
science.add_student(alice)

# Print out the courses for each student
print(alice.name, "is taking", alice.courses)
print(bob.name, "is taking", bob.courses)
print(charlie.name, "is taking", charlie.courses)

# Print out the students in each course
print(math.name, "has", math.students)
print(english.name, "has", english.students)
print(science.name, "has", science.students)