flag = "Y"

while flag == "Y":
    
    userChoice = int(input("Type a year and let's see if its a leap year!?\n"))

    if userChoice %4 == 0:
        if userChoice %400 == 0 or userChoice %100 != 0:
            print("It's a leap year!!")
        else:
            print("Not a Leap Year:(")
    else:
        print("Not a Leap Year:(")

    flag = input("Type Y to play again. Or N if you're done: ")