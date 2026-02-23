def check_grades(score):
   
    if score >= 90:
        return "A"
    elif score>= 80:
        return "B"
    elif score >= 70:
        return "C" 
    else:
        return "F"
while True:
    try:
        score = int(input("Enter your score:"))
        break
    except ValueError:
        print ("Invalid input. Please enter a number.")

grade = check_grades(score)

print(f"Your Grade is: {grade}")