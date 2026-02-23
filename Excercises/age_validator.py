def get_valid_age():

    while True:
        try:
            age_input = int(input("Please enter your age: "))
            if 1<= age_input <= 120:
             return age_input
            else:
                print("Invalid input. Please enter a valid age between 1 and 120.")

        except ValueError:
            print("Invalid Input. Please enter an integer value for age")
            
age= get_valid_age()
print(f"Your age is: {age}")    
       
