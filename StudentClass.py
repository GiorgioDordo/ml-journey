class StudentClass:
  def __init__(self, name, gradesList):
    self.name = name
    self.gradesList = gradesList

  def calculate_average(self):
    total = sum(self.gradesList)
    average = total / len(self.gradesList)
    return average

Jon = StudentClass("Jon", [85, 90, 78])  
print(Jon.calculate_average())