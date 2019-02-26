class Student:
    student_count = 0
    def __init__(self,Name,Age,Marks):
        self.Name = Name
        self.Age = Age
        self.Marks = Marks
    student_count += 1

    def studentcount(self):
        print("Student count: " + str(Student.student_count))

    def student_details(self):
        print("Name: " + self.Name + " Age: " + str(self.Age) + " Marks: " + str(self.Marks))

    def compare_marks(self,student2):
        if self.Marks > student2.Marks:
            print("Marks of Student1 is greater than Student2")
        else:
            print("Marks of Student2 is greater than Student1")
        return Student("name",20,self.Marks + student2.Marks)





Student1 = Student("Arjun",29,400)
Student2 = Student("Vijayan",30,500)

Student1.student_details()
Student2.student_details()

s3 = Student1.compare_marks(Student2)
print(hasattr(Student2,"Name"))
print(getattr(Student2,"Name"))
setattr(Student2,"Name","Ajay")
print(Student2.Name)