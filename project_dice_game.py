import random
score = 0
print("WELCOME TO THE DICE GAME!!!!!") #HEADING INDICATING STARTING OF THE GAME
print("Input 0 whenever you wish to exit.") #INSTRUCTION FOR EXITING THE GAME( HIGHLIGHTING THE BREAK CONDITION )
print(" ")
while True:                     # initiated an infinite loop that will take input from the user as long as the break condition is not hit
                                          # and will compare the value entered by the user and the value came up on the dice,
    choice = int(input("Select a number between 1 to 6 : "))
    dice = random.randint(1, 6) #IMPORTING THE RANDOM MODULE  AND USING IT TO GENERATE A NEW INTEGER BETWEEN 1 AND 6
                                                         # EACH TIME THE LOOP RUNS
    if choice == 0: #BREAK CONDITION
        print(" ")
        print("The game has ended, thankyou for joining!!!") #SEE OFF STATEMENT
        break
    print("The die value is :",dice)

    if choice !=0 and choice < 1 or choice >6: #INVALID INPUT CONDITION( IF THIS HITS THEN THE PROGRAM WILL JUST
        # PRINT "Invalid Input" AND THE CURRENT SCORE AND THEN RERUN THE LOOP)
        print("Invalid input")
        print("Please enter a valid input.")
        print("Your current score is :", score)
        print(" ")
    elif choice == dice: #CONDITION OF GAINING A POINT
        print("Hurray! you gained a point......")
        score+=1
        print("Your current score is :",score)
        print(" ")
    else: #CONDITION OF NO POINT GAIN
        print("Sorry! the numbers don't match, keep trying!!!")
        print("Your current score is :",score)
        print(" ")
print("Your final score is : ",score)