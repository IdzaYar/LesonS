class TooManyStudentsError(Exception):
    def __init__(self, message="Група повна."):
        self.message = message
        super().__init__(self.message)

class Group:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        if len(self.students) >= 10:
            raise TooManyStudentsError()
        else:
            self.students.append(student)

group = Group()
for i in range(10):
    group.add_student(f"Student {i+1}")

try:
    group.add_student("Student 11")
except TooManyStudentsError as e:
    print(e)
