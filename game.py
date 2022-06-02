import random

print("Guess a number between 1 and 9")

chances = 5
number = random.randint(1,10)

while (chances != 0) :
    guess = int(input("Enter your guess: "))
    if(guess == number) :
        print("YOU WIN!!!")
        break
    elif (guess < number) :
        print("Your guess was too low, try again")        
    elif (guess > number) :
        print("Your guess was too high, try again")
        
    chances = chances - 1
    
if chances == 0 :
    print("YOU LOSE!! the number is", number)