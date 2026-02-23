import random
choices = ["rock", "paper", "scissor"]

while True:
        computer_choice = random.choice(choices)    

        print ("Please choose\n 1.rock\n 2.paper\n 3.scissor\n")
        user_choice = (input())
        if user_choice not in choices:
          print("Invalid choice!")
          continue
        print(f"Computer choice: {computer_choice} ")
        if user_choice == "rock" and computer_choice == "scissor":
         print ("You Win")
        elif user_choice == "paper" and computer_choice == "scissor":
         print ("Computer Win")
        elif user_choice == "scissor" and computer_choice == "rock":
         print ("Computer win")
        elif user_choice == "scissor" and computer_choice == "paper":
         print ("You win")
        elif user_choice == "rock" and computer_choice == "paper":
         print ("computer win")
        elif user_choice == "paper" and computer_choice == "rock":
         print ("You win")
        else:
         print ("Tie")

        play_again = input("Do u want to play again: y/n")
        if play_again == "n":
          print("GoodBye!")
          break

        
        
    
      
    