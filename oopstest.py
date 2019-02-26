class Student:
    student_count = 10
    __student_count = 2
    def studentcount(self):
        Student.student_count +=10
        print("Student count: " + str(Student.student_count))
        print(self.student_count)

    def student_details(self):
        print("Name: " + self.Name + " Age: " + str(self.Age) + " Marks: " + str(self.Marks))

    def compare_marks(self,student2):
        if self.Marks > student2.Marks:
            print("Marks of Student1 is greater than Student2")
        else:
            print("Marks of Student2 is greater than Student1")
        return Student("name",20,self.Marks + student2.Marks  )





student1 = Student()
student2 = Student()

# print(Student.__student_count)
# print(student1.Name)

print(Student._Student__student_count)

student1.newtest = 5
#
# print(student1.newtest)
# print(Student.student_count)


# student1.studentcount()
#
# student2.studentcount()


#
# Student1.student_details()
# Student2.student_details()
#
# s3 = Student1.compare_marks(Student2)
# print(hasattr(Student2,"Name"))
# print(getattr(Student2,"Name"))
# setattr(Student2,"Name","Ajay")
# print(Student2.Name)

student1.studentcount()


# setattr(student1, '__student_count', 7000)

print(student1.__dict__)
print(Student.__dict__)
student1.studentcount()
