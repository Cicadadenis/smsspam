# -*- coding: utf-8 -*-
#!/bin/env python3
# 194-67-90-149
import os, sys
import time
import io
import getopt
import subprocess
import time
import signal
#import requests
#from requests import get


os.system('apt update')
print("update OK!!")
os.system('apt install python3-pip -y')
print("python3-pip OK!!")
os.system('apt install screen -y')
print("screen OK!!")
os.system('pip install requests')
print("requests OK!!")
os.system('apt install figlet -y ')
print("figlet OK!!")
os.system('pip install aiogram')
print("aiogram OK!!")
os.system('pip install PyYAML')
print("pyyaml OK!!")
os.system('pip install rich')
print("rich OK!!")



IP_API = "https://api.ipify.org/?format=json"

LATEST_RELEASE_API = "https://github.com/Cicadadenis/tor-cicada/blob/main/tor-cicada.py"






os.system('clear')
re = "\033[1;31m"
gr = "\033[1;32m"
cy="\033[1;36m"

logo = (f"""
          _             __         {re}___       __{cy}
     ____(_)______ ____/ /__ _____{re}/ _ )___  / /_{cy}
    / __/ / __/ _ `/ _  / _ `/___{re}/ _  / _ \/ __/{cy}
    \__/_/\__/\_,_/\_,_/\_,_/   {re}/____/\___/\__/{cy}

    ----------Telegram-Bot-PhotoHosting-----------



    """)
re = "\033[1;31m"
gr = "\033[1;32m"
cy = "\033[1;36m"
print(logo)
print(f"""
               {gr}+-+-+-+-+-+ +-+-+-+-+{cy}
               {gr}|T|o|k|e|n| |B|o|t|a|{cy}
               {gr}+-+-+-+-+-+ +-+-+-+-+{cy}
 """)
token = input('⏩⏩⏩ ')
os.system('clear')
print(logo)
message_bot = 'Начать беседу со мной'
#message_bot = input(f"{re}\nТекст вспомогательной кнопки /start: ")
os.system('clear')

data = {'bot': {'token': token,
                'parse_mode': 'html'}, 'executor': {'skip_updates':
                True}, 'modules': ['handlers.main', 'handlers.errors'],
                'log_ignore': ['aiogram', 'asyncio', 'aiogram.Middleware'],
                'commands': {'start': message_bot}}

with io.open('config.yaml', 'w', encoding='utf8') as outfile:
    yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)
    import requests

MethodGetMe = (f'''https://api.telegram.org/bot{token}/GetMe''')
response = requests.post(MethodGetMe)
tttm = response.json()


id_us = (tttm['result']['id'])
first_name = (tttm['result']['first_name'])
username = (tttm['result']['username'])
os.system('chmod +x *')
print(logo)

print(f"""

            ---------------------------------
               🆔 Твой id: {id_us}
            ---------------------------------
               👤 Имя Бота: {first_name}
            ---------------------------------
               🗣 username: {username}
            ---------------------------------
              🌐 https://t.me/{username}
            ---------------------------------
            ******* Suport: @Satanasat ******
""")
input("Для запуска бота нажми Enter")
os.system('./ini.sh')
