import random
def guess_number():
    secret=random.randint(1,100)
    number=int(input("Guess a number between 1 and 100:"))
    count=0
    while True:
        
        if(number>100 or number <1):
            print("Number out of bounds!") 
        else:
            count += 1
            if number==secret:
                break
            elif(number>secret):
                print("Too high!")
            else:
                print("Too low!")
        number=int(input("Guess again: "))
    print("You guessed it right! , you took ",count,"guesses.")
    print("The secret number was: ",secret)

play_again="yes"
while play_again.lower()=="yes":
    guess_number()
    play_again=input("Would you like to play again? (yes/no)")
    

