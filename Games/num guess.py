import random

secret_number = random.randint(1, 10)
count = 0
while True:
    count += 1 
    try:
        guess = int(input("Guess the Number between 1 and 10:"))
        if guess < secret_number:
            print("Too low")
            
        elif guess > secret_number:
            print("Too high")
            
        else:
            print("Congratulations! You guessed the right number.")
            
            print(f"Number of attempts: {count}")
            break
    except ValueError:
        print("Invalid Input! Please enter an Integer Value.")
