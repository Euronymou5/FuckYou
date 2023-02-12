from colorama import Fore
import os
import platform
import re
import requests
import time
import shutil

def ser_menu():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")
  print(f"""{Fore.MAGENTA}
          ▄• ▄▌.▄▄ · ▄▄▄ .▄▄▄      .▄▄ · ▄▄▄ . ▄▄▄· ▄▄▄   ▄▄·  ▄ .▄
          █▪██▌▐█ ▀. ▀▄.▀·▀▄ █·    ▐█ ▀. ▀▄.▀·▐█ ▀█ ▀▄ █·▐█ ▌▪██▪▐█
          █▌▐█▌▄▀▀▀█▄▐▀▀▪▄▐▀▀▄     ▄▀▀▀█▄▐▀▀▪▄▄█▀▀█ ▐▀▀▄ ██ ▄▄██▀▐█
          ▐█▄█▌▐█▄▪▐█▐█▄▄▌▐█•█▌    ▐█▄▪▐█▐█▄▄▌▐█ ▪▐▌▐█•█▌▐███▌██▌▐▀
           ▀▀▀  ▀▀▀▀  ▀▀▀ .▀  ▀     ▀▀▀▀  ▀▀▀  ▀  ▀ .▀  ▀·▀▀▀ ▀▀▀ ·                                               
  |--------------------------------------------------------------------------------------------|
  | [1] Sherlock - Encuentra distintos usuarios registrados en varias redes sociales.          |
  | [2] Nexfil - Una herramienta OSINT para encontrar perfiles por nombre de usuario           |
  | [3] XR-Search - Herramienta de busquedas de usuarios, propia de Fuckyou!                   |
  | [00] Regresar Al Menu Principal                                                            |
  | [99] Salir                                                                                 |
  |--------------------------------------------------------------------------------------------|
  """)
  var = input(f'\n{Fore.CYAN}root@fuckyou:~# ')
  # Sherlock ---
  if var == "1":
    if os.path.exists('tools/sherlock'):
      print(f'\n{Fore.RED}[!] Sherlock ya existe')
      ques = input(f'\n{Fore.GREEN}[?] Quieres iniciar la herramienta [Y/n]: ')
      if ques == "Y" or ques == "y":
        usuario = input('\n[~] Ingresa un nombre de usuario: ')
        if usuario == "" or usuario == " ":
            print(f'\n{Fore.RED}[!] Error debes de ingresar un usuario.')
        else:
            if platform.system() == "Linux":
              os.system(f"python3 tools/sherlock/sherlock/sherlock.py {usuario}")
            else:
                os.system(f"python tools/sherlock/sherlock/sherlock.py {usuario}")
      elif ques == "N" or ques == "n":
        ser_menu()
      else:
        ser_menu()
    else:
      if platform.system() == "Linux":
        print(f'\n{Fore.GREEN}[~] Instalando Sherlock...')
        os.system("git clone https://github.com/sherlock-project/sherlock.git && mv 'sherlock' tools/ && pip3 install -r tools/sherlock/requirements.txt")
        print('\n[~] Sherlock instalado con exito.')
        time.sleep(2)
        ser_menu()
      else:
        print(f'\n{Fore.GREEN}[~] Instalando Sherlock...')
        os.system("git clone https://github.com/sherlock-project/sherlock.git")
        shutil.move("sherlock/", "tools")
        os.system("python -m pip install -r tools/sherlock/requirements.txt")
        print('\n[~] Sherlock instalado con exito.')
        time.sleep(2)
        ser_menu()
  # nexfil --
  elif var == "2":
    if os.path.exists('tools/nexfil'):
      print(f'\n{Fore.RED}[!] Nexfil ya existe')
      ques = input(f'\n{Fore.GREEN}[?] Quieres iniciar la herramienta [Y/n]: ')
      if ques == "Y" or ques == "y":
        usuario = input('\n[~] Ingresa un nombre de usuario: ')
        os.chdir('tools/nexfil')
        os.system(f"python3 nexfil.py -u {usuario}")
      elif ques == "N" or ques == "n":
        ser_menu()
      else:
        ser_menu()
    else:
      if platform.system() == "Linux":
        print(f'\n{Fore.GREEN}[~] Instalando Nexfil...')
        os.system("git clone https://github.com/thewhiteh4t/nexfil.git && mv 'nexfil' tools/ && pip3 install -r tools/nexfil/requirements.txt")
        print('\n[~] Nexfil instalado con exito.')
        time.sleep(2)
        ser_menu()
      else:
       print(f'\n{Fore.RED}[!] Nexfil no esta disponible para tu sistema operativo.')
  # XR-Search  ------
  elif var == "3":
     if os.name == "nt":
         os.system("cls")
     else:
         os.system("clear")
     logo = f"""{Fore.BLUE}
      ██   ██ ██████        ███████ ███████  █████  ██████   ██████ ██   ██ 
       ██ ██  ██   ██       ██      ██      ██   ██ ██   ██ ██      ██   ██ 
        ███   ██████  █████ ███████ █████   ███████ ██████  ██      ███████ 
       ██ ██  ██   ██            ██ ██      ██   ██ ██   ██ ██      ██   ██ 
      ██   ██ ██   ██       ███████ ███████ ██   ██ ██   ██  ██████ ██   ██"""
     print(logo)
     usuario = input('\n[~] Ingresa el nombre del usuario: ')
     sites = [f"https://github.com/{usuario}", f"https://twitter.com/{usuario}", f"https://instagram.com/{usuario}", f"https://www.reddit.com/user/{usuario}", f"https://www.pinterest.com/{usuario}", f"https://www.twitch.tv/{usuario}", f"https://xboxgamertag.com/search/{usuario}", f"https://open.spotify.com/user/{usuario}", f"https://www.roblox.com/user.aspx?username={usuario}", f"https://t.me/{usuario}", f"https://xvideos.com/profiles/{usuario}", f"https://www.youtube.com/user/{usuario}", f"https://gitlab.com/{usuario}", f"https://api.mojang.com/users/profiles/minecraft/{usuario}", f"https://www.codecademy.com/profiles/{usuario}", f"https://www.codewars.com/users/{usuario}", f"https://forum.hackthebox.eu/profile/{usuario}", f"https://replit.com/@{usuario}"]
     for url in sites:
        pagina = requests.get(url)
        final = re.findall(usuario, pagina.text)
        if final:
            print(f'\n{Fore.GREEN}[  ✔️   ] Usuario encontrado! {url}')
        else:
            print(f'\n{Fore.RED}[!] Usuario no encontrado')
  # 00
  elif var == "00":
    if platform.system() == "Linux":
       os.system("python3 fuckyou.py")
    elif platform.system() == "Windows":
       os.system("python fuckyou.py")
    else:
      exit()
  # exit
  elif var == "99":
    exit()
  # error no input
  else:
    print(f'\n{Fore.RED}[!] Error opcion invalida.')
    time.sleep(2)
    phish()
