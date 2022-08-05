N = int(input())

class Student:
  def __init__(self, name, korean, english, math):
    self.name = name
    self.korean = int(korean)
    self.english = int(english)
    self.math = int(math)

student_list = []

for _ in range(N):
  data = input().split()
  student = Student(*data)
  student_list.append(student)

student_list.sort(key = lambda s: (-s.korean, s.english, -s.math, s.name))
for student in student_list:
  print(student.name)

  ## 굳굳