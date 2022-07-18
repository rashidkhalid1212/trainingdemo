import random
randNumber = random.randint(1, 100)
userguess = None
guesses = 0

while(userguess != randNumber):
    userguess = int(input("Enter your guess: "))
    guesses += 1

    if(userguess == randNumber):
        print("you guessed it right!")
    else:
        if(userguess>randNumber):
                print("you guessed wrong! Try a smaller number")
        else:
            print("you guessed it wrong! Try a bigger number")
            
print(f"You guessed the number in {guesses} guesses")

with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if(guesses < hiscore):
    print("You have broken the record")
    with open("highscore.txt", "w") as f:
        f.write(str(guesses))