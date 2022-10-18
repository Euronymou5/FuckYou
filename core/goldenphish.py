from colorama import Fore
import os
import platform
import time
import shutil

def phish():
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")
  print(f"""{Fore.MAGENTA}

          ██████╗ ██╗  ██╗██╗███████╗██╗  ██╗██╗███╗   ██╗ ██████╗ 
          ██╔══██╗██║  ██║██║██╔════╝██║  ██║██║████╗  ██║██╔════╝ 
          ██████╔╝███████║██║███████╗███████║██║██╔██╗ ██║██║  ███╗
          ██╔═══╝ ██╔══██║██║╚════██║██╔══██║██║██║╚██╗██║██║   ██║
          ██║     ██║  ██║██║███████║██║  ██║██║██║ ╚████║╚██████╔╝
          ╚═╝     ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 
                                                         
  |--------------------------------------------------------------------------------------------|
  | [1] SayCheese - Herramienta Para Obtener IP Y Una Captura Por Medio De La WebCam.          |
  | [2] Zphisher  - Herramienta Con Mas De 30 Templates De Paginas Login.                      |
  | [3] 0ni-Phish - Tool Que Cuenta Con 10 Templates De Paginas Login, 4 De Ellas En Español!! |
  | [4] PyPhisher - Herramienta CON MAS DE 50 Templates De Paginas Login!!!!                   |
  | [00] Regresar Al Menu Principal                                                            |
  | [99] Salir                                                                                 |
  |--------------------------------------------------------------------------------------------|
  """)
  var = input(f'\n{Fore.CYAN}root@fuckyou:~# ')
  # SayCheese ---
  if var == "1":
    if os.path.exists('tools/saycheese'):
      print(f'\n{Fore.RED}[!] SayCheese ya existe')
      ques = input(f'\n{Fore.GREEN}[?] Quieres iniciar la herramienta [Y/n]: ')
      if ques == "Y" or ques == "y":
        os.system("bash tools/saycheese/saycheese.sh")
      elif ques == "N" or ques == "n":
        phish()
      else:
        phish()
    else:
      if platform.system() == "Linux":
        print(f'\n{Fore.GREEN}[~] Instalando SayCheese...')
        os.system("git clone https://github.com/hangetzzu/saycheese && mv 'saycheese' tools/")
        print('\n[~] SayCheese instalado con exito.')
        time.sleep(2)
        phish()
      else:
       print(f'\n{Fore.RED}[!] SayCheese no esta disponible para tu sistema operativo.')
  # Zphisher --
  elif var == "2":
    if os.path.exists('tools/zphisher'):
      print(f'\n{Fore.RED}[!] Zphisher ya existe')
      ques = input(f'\n{Fore.GREEN}[?] Quieres iniciar la herramienta [Y/n]: ')
      if ques == "Y" or ques == "y":
        os.chdir('tools/zphisher')
        os.system("bash zphisher.sh")
        os.chdir('..')
        os.chdir('..')
        os.system("python3 fuckyou.py")
      elif ques == "N" or ques == "n":
        phish()
      else:
        phish()
    else:
      if platform.system() == "Linux":
        print(f'\n{Fore.GREEN}[~] Instalando Zphisher...')
        os.system("git clone https://github.com/htr-tech/zphisher && mv 'zphisher' tools/")
        print('\n[~] Zphisher instalado con exito.')
        time.sleep(2)
        phish()
      else:
       print(f'\n{Fore.RED}[!] Zphisher no esta disponible para tu sistema operativo.')
  # 0ni-Phish  ------
  elif var == "3":
    if os.path.exists('tools/0ni-Phish'):
      print(f'\n{Fore.RED}[!] 0ni-Phish ya existe')
      ques = input(f'\n{Fore.GREEN}[?] Quieres iniciar la herramienta [Y/n]: ')
      if ques == "Y" or ques == "y":
        if platform.system() == "Linux":
           os.system("python3 tools/0ni-Phish/0ni.py")
      elif ques == "N" or ques == "n":
        phish()
      else:
        phish()
    else:
      if platform.system() == "Linux": 
        print(f'\n{Fore.GREEN}[~] Instalando 0ni-Phish...')
        os.system("git clone https://github.com/Euronymou5/0ni-Phish && mv '0ni-Phish' tools/")
        print('\n[~] 0ni-Phish instalado con exito.')
        time.sleep(2)
        phish()
      else:
       print(f'\n{Fore.RED}[!] 0ni-Phish no esta disponible para tu sistema operativo.')
  # PyPhisher ----
  elif var == "4":
    if os.path.exists('tools/PyPhisher'):
      print(f'\n{Fore.RED}[!] Pyphisher ya existe')
      ques = input(f'\n{Fore.GREEN}[?] Quieres iniciar la herramienta [Y/n]: ')
      if ques == "Y" or ques == "y":
        if platform.system() == "Linux":
           os.chdir('tools/PyPhisher')
           os.system("python3 pyphisher.py")
           os.chdir('..')
           os.chdir('..')
           os.system("python3 fuckyou.py")
      elif ques == "N" or ques == "n":
        phish()
      else:
        phish()
    else:
      if platform.system() == "Linux": 
        print(f'\n{Fore.GREEN}[~] Instalando PyPhisher...')
        os.system("git clone https://github.com/KasRoudra/PyPhisher && mv 'PyPhisher' tools/ && pip3 install -r tools/PyPhisher/files/requirements.txt")
        print('\n[~] PyPhisher instalado con exito.')
        time.sleep(2)
        phish()
      else:
       print(f'\n{Fore.RED}[!] PyPhisher no esta disponible para tu sistema operativo.')
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
