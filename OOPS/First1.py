class Student:
    def set_name(self,name):
        self.name=name  # class attribute

    def get_name(self):
        return self.name
student1= Student()
student1.set_name("Shukla")
print(student1.get_name())
student1.eng_marks = 45  # instance attribute
print(student1.eng_marks)

student2 = Student()
student2.set_name("Priya")
print(student2.get_name())