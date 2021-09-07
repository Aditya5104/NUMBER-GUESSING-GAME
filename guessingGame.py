import random
print ("Number Guessing game")
number=random.randint(1,9)
chances=0
print ("guess a number between 1 and 9")
while chances<5:
    guess=int(input("Enter Your Guess"))
    if guess==number:
        print("Congratulations! You won")
        break  
    elif guess>number:
        print("Your Guess was too high,Guess Lower number")     
    else:
        print("Your guess was too low, guess higher number")

    chances=chances+1    

if chances==5:
        print("You lost")

