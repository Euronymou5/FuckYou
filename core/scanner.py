from colorama import Fore
import os
import platform

def scan():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    print(f"""{Fore.MAGENTA}
   ▄████████  ▄████████    ▄████████ ███▄▄▄▄   ███▄▄▄▄      ▄████████    ▄████████ 
  ███    ███ ███    ███   ███    ███ ███▀▀▀██▄ ███▀▀▀██▄   ███    ███   ███    ███ 
  ███    █▀  ███    █▀    ███    ███ ███   ███ ███   ███   ███    █▀    ███    ███ 
  ███        ███          ███    ███ ███   ███ ███   ███  ▄███▄▄▄      ▄███▄▄▄▄██▀ 
▀███████████ ███        ▀███████████ ███   ███ ███   ███ ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
         ███ ███    █▄    ███    ███ ███   ███ ███   ███   ███    █▄  ▀███████████ 
   ▄█    ███ ███    ███   ███    ███ ███   ███ ███   ███   ███    ███   ███    ███ 
 ▄████████▀  ████████▀    ███    █▀   ▀█   █▀   ▀█   █▀    ██████████   ███    ███ 
                                                                        ███    ███ 

  |--------------------------------------------------------------------------------------------|
  | [1] Escaneo de Puertos                                                                     |
  | [2] Escaneo de Puertos Especificos                                                         |
  | [3] Escaneo de Puertos Con Version                                                         |
  | [4] Escaneo de Puertos Con Deteccion de Sistema Operativo                                  |
  | [5] Escaneo Rapido (Solo Puertos Abiertos)                                                 |
  | [6] Escaneo de Sub-Red                                                                     |
  | [7] Escaneo Silencioso                                                                     |
  | [8] Escaneo TCP Sincronizado                                                               |
  | [9] Escaneo UDP                                                                            |
  | [00] Regresar Al Menu Principal                                                            |
  | [99] Salir                                                                                 |
  |--------------------------------------------------------------------------------------------|
    """)
    var = input(f'\n{Fore.CYAN}root@fuckyou:~# ')
    if var == "1":
      target = input("\n[~] Ingrese el host o IP a escanear: ")
      os.system(f"nmap {target}")
    elif var == "2":
       target = input("\n[~] Ingrese el host o IP a escanear: ")
       ports = input("\n[~] Ingrese los puertos a escanear separados por comas (ej: 22,80,443): ")
       os.system(f"nmap -p {ports} {target}")
    elif var == "3":
       target = input("\n[~] Ingrese el host o IP a escanear: ")
       os.system(f"nmap -sV {target}")
    elif var == "4":
       target = input("\n[~] Ingrese el host o IP a escanear: ")
       os.system(f"nmap -O {target}")
    elif var == "5":
       target = input("\n[~] Ingrese el host o IP a escanear: ")
       os.system(f"nmap -F {target}")
    elif var == "6":
       subnet = input("\n[~] Ingrese la sub-red a escanear (ej: 8.8.8.8/24): ")
       os.system(f"nmap -sP {subnet}")
    elif var == "7":
       target = input("\n[~] Ingrese el host o IP a escanear: ")
       os.system(f"nmap -sS {target}")
    elif var == "8":
       target = input("\n[~] Ingrese el host o IP a escanear: ")
       os.system(f"nmap -sS -sV {target}")
    elif var == "9":
       target = input("\n[~] Ingrese el host o IP a escanear: ")
       os.system(f"nmap -sU {target}")
    elif var == "00":
       if platform.system() == "Linux":
          os.system("python3 fuckyou.py")
       elif platform.system() == "Windows":
         os.system("python fuckyou.py")
       else:
         exit()
    elif var == "99":
       exit()
