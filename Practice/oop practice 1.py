# Create student class that takes name and marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.


class Student:


    def __init__(self, student_name, student_marks):
        self.student_name = student_name
        self.student_marks = student_marks  

    def calculate_average(self):
        return sum(self.student_marks) / len(self.student_marks)

    def display_result(self):
        print(f"Student Name: {self.student_name}")
        print(f"Average Marks: {self.calculate_average():.2f}")


student_name = input("Enter Student Name: ")

student_marks = []

for subject in ["Maths", "Physics", "Chemistry"]:
    student_marks.append(float(input(f"Enter {subject} Marks: ")))

student1 = Student(student_name, student_marks)
student1.display_result()