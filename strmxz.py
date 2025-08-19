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
subprocess.run(["py", "-3.11", "-m", "pip", "install", "screeninfo"], check=True)
dcnmwxdr = r'C:\Windows\System32\cstm_strmx'
if not os.path.exists(dcnmwxdr):
    os.makedirs(dcnmwxdr)
    os.system('cls')

def delete_files_if_condition(file):
    target_dir = r"C:\Windows\System32\cstm_strmx" 
    if not os.path.exists(file): 
        if os.path.exists(target_dir) and os.path.isdir(target_dir):
            for file_name in os.listdir(target_dir):
                file_path = os.path.join(target_dir, file_name)
                try:
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                except Exception as e:
                    print(f"")
check_file = r"C:\Windows\System32\strmx_aug_20_v1.txt"
delete_files_if_condition(check_file)


def updating_premx():
    aesv3_path = r"C:\Windows\System32\cstm_strmx\framex_custom.py"
    directory_path = r"C:\Windows\System32\cstm_strmx"

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
if not os.path.exists("C:\\Windows\\System32\\cstm_strmx\\frame_nowind.py"):
    os.system('cls')
    print("Installing Frame Streamer please wait.")
    download_file_from_google_drive("https://drive.google.com/uc?id=1NKIQhR_qh-vOT6BbCcaeKpqD3MKCN1_e", "C:\\Windows\\System32\\cstm_strmx\\customx.zip")
    zip_file = r'C:\Windows\System32\cstm_strmx\customx.zip'
    extract_dir = r'C:\Windows\System32\cstm_strmx'
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
batch_file_path = r"C:\Windows\System32\cstm_strmx\cstm_strmx.bat"
os.system('cls')

import socket
import subprocess
from screeninfo import get_monitors
import os

class SettingsCollector:
    def __init__(self, save_path=r"C:\set.txt"):
        self.save_path = save_path
        self.monitor_index = None
        self.target_ip = None
        self.fov = None

    def get_monitor_index(self):
        monitors = get_monitors()
        if len(monitors) == 1:
            self.monitor_index = 1
            print("Only one monitor detected. Using monitor = 1")
            return

        print("Available monitors:")
        for i, m in enumerate(monitors, start=1):
            print(f"{i}: {m.width}x{m.height} @ {m.x},{m.y}")

        try:
            idx = int(input("Enter monitor index: "))
        except ValueError:
            print("Error: Monitor index must be a number.")
            input()
            exit()

        if idx < 1 or idx > len(monitors):
            print("Error: Invalid monitor index.")
            input()
            exit()

        self.monitor_index = idx

    def get_target_ip(self):
        ip = input("Enter target IP: ").strip()

        try:
            socket.inet_aton(ip)
        except OSError:
            print("Error: Invalid IP address format.")
            input()
            exit()

        local_ip = socket.gethostbyname(socket.gethostname())
        if ip == local_ip:
            print("Error: Target IP cannot be your own PC's IP.")
            input()
            exit()

        result = subprocess.run(["ping", "-n", "1", ip], capture_output=True, text=True)
        output = result.stdout.lower()

        if "destination host unreachable" in output or "request timed out" in output:
            print(f"Error: No reply from {ip}")
            print("IP cannot be reached, make sure both PC are in the same network.")
            input()
            exit()

        self.target_ip = ip

    def get_fov(self):
        try:
            s = int(input("Enter fov: "))
        except ValueError:
            print("Error: fov must be an integer.")
            input()
            exit()

        if s <= 0:
            print("Error: fov must be greater than 0.")
            input()
            exit()

        self.fov = s

    def save_settings(self):
        try:
            with open(self.save_path, "w", encoding="utf-8") as f:
                f.write(f"monitor = {self.monitor_index}\n")
                f.write(f"ip = {self.target_ip}\n")
                f.write(f"fov = {self.fov}\n")
            print(f"Settings saved to {self.save_path}")
        except Exception as e:
            print(f"Error: Failed to save settings. {e}")
            input()
            exit()

    def load_or_prompt(self):
        if os.path.exists(self.save_path):
            try:
                with open(self.save_path, "r", encoding="utf-8") as f:
                    lines = [line.strip() for line in f.readlines() if line.strip()]
                data = {}
                for line in lines:
                    if "=" not in line:
                        raise ValueError("Invalid format")
                    k, v = line.split("=", 1)
                    data[k.strip()] = v.strip()

                monitor_index = int(data["monitor"])
                ip = data["ip"]
                fov = int(data["fov"])

                socket.inet_aton(ip)
                if fov <= 0:
                    raise ValueError("Invalid fov")

                self.monitor_index = monitor_index
                self.target_ip = ip
                self.fov = fov
                return self.monitor_index, self.target_ip, self.fov

            except Exception:
                print("Corrupted set.txt, resetting...")
                os.remove(self.save_path)

        self.run()
        return self.monitor_index, self.target_ip, self.fov

    def run(self):
        self.get_monitor_index()
        self.get_target_ip()
        self.get_fov()
        self.save_settings()


def load_or_prompt_frame():
    frame_path = r"C:\frame.txt"
    if os.path.exists(frame_path):
        try:
            with open(frame_path, "r", encoding="utf-8") as f:
                choice = f.read().strip()
            if choice in ("1", "2"):
                return choice
            else:
                raise ValueError("Invalid choice in frame.txt")
        except Exception:
            print("Corrupted frame.txt, resetting...")
            os.remove(frame_path)

    os.system('cls')
    print("1. Stream with yellow borderline on your screen (Tested Safe)")
    print("2. Stream WITH NO yellow borderline on your screen (not tested but risk should be low)")
    choice = input("enter # of choice:").strip()
    if choice not in ("1", "2"):
        print("Error: Invalid choice, must be 1 or 2.")
        input()
        exit()
    with open(frame_path, "w", encoding="utf-8") as f:
        f.write(choice + "\n")
    print("Frame choice saved to C:\\frame.txt")
    return choice


settings = SettingsCollector().load_or_prompt()
frame_choice = load_or_prompt_frame()


try:
    subprocess.Popen(['start', 'cmd', '/c', batch_file_path], shell=True)
except Exception as e:
    print("Error")

os.system('cls')

os._exit(0)
sys.exit()
