from models.person import Person

class Student(Person):
    def __init__(self, pid, name, age, student_id):
        super().__init__(pid, name, age, student_id)
        self.student_id = student_id
        
    def __str__(self):
        return f"student[ {self.pid} , Name : {self.name} , Age : {self.age} , Student ID : {self.student_id}]"