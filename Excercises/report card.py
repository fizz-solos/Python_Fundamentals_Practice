def get_grade(score):
  if score >= 80:
   return "A"
  elif score >= 60:
   return "B"
  elif score >= 50:
   return "C"
  else:
   return "F"
  
students = {
    "Ali": 88,
    "Sara": 45,
    "James": 72,
    "Mia": 95,
    "Tom": 55
}

for name, score in students.items():
 print (f"{name} - score:{score} - Grade:{get_grade(score)}")
passing_students = [name for name, score in students.items() if score >= 50]
print (f"Students who passed: {passing_students}")

def class_average(students):
 return sum(students.values())/len(students)

print(class_average(students))