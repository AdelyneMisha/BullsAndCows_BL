import random

def generateNumber():
    n = ''.join(random.choices('123456789', k=4))
    while len(set(n)) < 4:
        n = ''.join(random.choices('123456789', k=4))
    return n

print("Welcome to Bulls and Cows!")
print("Try to guess the 4-digit number with unique digits.")

number = generateNumber()

while True:
    guess = input("Enter your guess: ")
    
    if len(guess) != 4 or not guess.isdigit():
        print("Invalid input. Please enter a 4-digit number.")
        continue

    bulls = sum(1 for i in range(4) if guess[i] == number[i])
    
    cows = 0
    number_copy = list(number)
    
    for i in range(4):
        if guess[i] == number[i]:
            number_copy[i] = None

    for i in range(4):
        if guess[i] in number_copy and number_copy.count(guess[i]) > 0:
            cows += 1
            number_copy[number_copy.index(guess[i])] = None

    print(f"Bulls: {bulls}, Cows: {cows}")
    
    if bulls == 4:
        print("Congratulations! You've guessed the number.")
        break
