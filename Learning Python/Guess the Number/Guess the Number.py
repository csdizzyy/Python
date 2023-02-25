from random import randrange

number = randrange(1000)
attempts = 0
guess = 0

while guess != number:
        
    attempts += 1
    guess = int(input("Your guess: "))
    
    if guess > number:
        print("Too High")
    if guess < number:
        print("Too Low")
    
print("You won in " + str(attempts) + " attempts!")