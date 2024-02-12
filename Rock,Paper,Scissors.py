import random as rd

flag = 'Y'

pcWin = 0
userWin = 0
tie = 0

while flag == "Y":
    print("Lets Play Rock Paper Scissors!!!")

    pc_choice = rd.choice(['Rock','Paper','Scissors'])

    user_choice = input("Choose 'Rock', 'Paper', or 'Scissors': ")

    print(f"PC chose: " + pc_choice)

    if user_choice == 'Rock' and pc_choice =='Scissors' or user_choice == 'Scissors' and pc_choice == 'Paper' or user_choice == 'Paper' and pc_choice == 'Rock':
        print("You won!! Wanna play again?")
        userWin += 1
        print(f"I have won {pcWin} rounds, you have won {userWin} rounds, we've tied {tie} rounds")
    elif user_choice == 'Rock' and pc_choice == 'Paper' or user_choice == 'Scissors' and pc_choice == 'Rock' or user_choice == 'Paper' and pc_choice == 'Scissors':
        print("I won!! Let's play again if you're not scared")
        pcWin += 1
        print(f"I have won {pcWin} rounds, you have won {userWin} rounds, we've tied {tie} rounds")
    else:
        print("We tied :( Wanna play again?")
        tie += 1
        print(f"I have won {pcWin} rounds, you have won {userWin} rounds, we've tied {tie} rounds")

    flag = input("Type Y if you wanna play again, type N if you're done: ")