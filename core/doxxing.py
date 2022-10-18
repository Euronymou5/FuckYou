from colorama import Fore
import os
import platform
import time
import shutil


def doxxer():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    print(f"""{Fore.RED}
        ▄▀▀█▄▄   ▄▀▀▀▀▄   ▄▀▀▄  ▄▀▄  ▄▀▀▄  ▄▀▄  ▄▀▀█▀▄    ▄▀▀▄ ▀▄  ▄▀▀▀▀▄   
        █ ▄▀   █ █      █ █    █   █ █    █   █ █   █  █  █  █ █ █ █         
        ▐ █    █ █      █ ▐     ▀▄▀  ▐     ▀▄▀  ▐   █  ▐  ▐  █  ▀█ █    ▀▄▄  
          █    █ ▀▄    ▄▀      ▄▀ █       ▄▀ █      █       █   █  █     █ █ 
         ▄▀▄▄▄▄▀   ▀▀▀▀       █  ▄▀      █  ▄▀   ▄▀▀▀▀▀▄  ▄▀   █   ▐▀▄▄▄▄▀ ▐ 
        █     ▐             ▄▀  ▄▀     ▄▀  ▄▀   █       █ █    ▐   ▐         
        ▐                  █    ▐     █    ▐    ▐       ▐ ▐                  
  |--------------------------------------------------------------------------------------------|
  | [1] Doxxer-Toolkit - Kit completo de doxxing para linux y termux.                          |
  | [2] Garuda  - Tool de doxxing para: nombre completo, ip, numero de telefono.               |
  | [3] LineX - Tool para obtener informacion de un numero de telefono.                        |
  | [4] IPlogger - IPlogger desde terminal para linux y termux.                                |
  | [00] Regresar al menu principal                                                            |
  | [99] Salir                                                                                 |
  |--------------------------------------------------------------------------------------------|
  """)
    var = input(f'\n{Fore.BLUE}root@fuckyou:~# ')
    # Doxxer-toolkit ---
    if var == "1":
        if os.path.exists('tools/Doxxer-Toolkit'):
            print(f'\n{Fore.RED}[!] Doxxer-Toolkit ya existe')
            ques = input(
                f'\n{Fore.GREEN}[?] Quieres iniciar la herramienta [Y/n]: ')
            if ques == "Y" or ques == "y":
                os.system("python3 tools/Doxxer-Toolkit/dox.py")
            elif ques == "N" or ques == "n":
                doxxer()
            else:
                doxxer()
        else:
            if platform.system() == "Linux":
                print(f'\n{Fore.GREEN}[~] Instalando Doxxer-Toolkit...')
                os.system(
                    "git clone https://github.com/Euronymou5/Doxxer-Toolkit && mv 'Doxxer-Toolkit' tools/ && bash tools/Doxxer-Toolkit/install.sh"
                )
                print('\n[~] Doxxer-Toolkit instalado con exito.')
                time.sleep(2)
                doxxer()
            else:
                print(
                    f'\n{Fore.RED}[!] Doxxer-Toolkit no esta disponible para tu sistema operativo.'
                )
    # Garuda --
    elif var == "2":
        if os.path.exists('tools/Garuda'):
            print(f'\n{Fore.RED}[!] Garuda ya existe')
            ques = input(
                f'\n{Fore.GREEN}[?] Quieres iniciar la herramienta [Y/n]: ')
            if ques == "Y" or ques == "y":
                print("""
        Argumentos:

        --name     Doxxear nombre completo

        --ip       Doxxear una direccion IP

        --mail     Doxxear un email

        --phone    Doxxear un numero de telefono

        --user     Doxxear un nombre de usuario
        """)
                arg = input(
                    f'{Fore.BLUE}\n[~] Ingresa un argumento de garuda: ')
                if arg == "--name" or arg == "--ip" or arg == "--mail" or arg == "--phone" or arg == "--user":
                    os.system(f"python3 tools/Garuda/garuda.py {arg}")
                else:
                    print(
                        f'\n{Fore.RED}[!] Error debes ingresar un argumento.')
                    time.sleep(2)
                    doxxer()
            elif ques == "N" or ques == "n":
                doxxer()
            else:
                doxxer()
        else:
            if platform.system() == "Linux":
                print(f'\n{Fore.GREEN}[~] Instalando Garuda...')
                os.system(
                    "git clone https://github.com/noob-coder123/Garuda && mv 'Garuda' tools/ && pip install -r tools/Garuda/requirements.txt "
                )
                print(f'\n[~] Garuda instalado con exito.')
                time.sleep(2)
                doxxer()
            else:
                print(
                    f'\n{Fore.RED}[!] Garuda no esta disponible para tu sistema operativo.'
                )
    # LineX  ------
    elif var == "3":
        if os.path.exists('tools/LineX'):
            print(f'\n{Fore.RED}[!] LineX ya existe')
            ques = input(
                f'\n{Fore.GREEN}[?] Quieres iniciar la herramienta [Y/n]: ')
            if ques == "Y" or ques == "y":
                if platform.system() == "Linux":
                    os.system("python3 tools/LineX/linex.py")
                elif platform.system() == "Windows":
                    os.system("python tools/LineX/linex_win.py")
            elif ques == "N" or ques == "n":
                doxxer()
            else:
                doxxer()
        else:
            if platform.system() == "Linux":
                print(f'\n{Fore.GREEN}[~] Instalando LineX...')
                os.system(
                    "git clone https://github.com/Euronymou5/LineX.git && mv 'LineX' tools/ && pip install requests"
                )
                print('\n[~] LineX instalado con exito.')
                time.sleep(2)
                doxxer()
            elif platform.system() == "Windows":
                print(f'\n{Fore.GREEN}[~] Instalando LineX...')
                os.system("git clone https://github.com/Euronymou5/LineX.git")
                shutil.move("LineX/", "tools")
                os.system("pip install requests")
                print('\n[~] LineX instalado con exito.')
                time.sleep(2)
                doxxer()
            else:
                print(
                    f'\n{Fore.RED}[!] LineX no esta disponible para tu sistema operativo.'
                )
    # IPlogger ----
    elif var == "4":
        if os.path.exists('tools/IPlogger'):
            print(f'\n{Fore.RED}[!] IPlogger ya existe')
            ques = input(
                f'\n{Fore.GREEN}[?] Quieres iniciar la herramienta [Y/n]: ')
            if ques == "Y" or ques == "y":
                os.system("python3 tools/IPlogger/run.py")
            elif ques == "N" or ques == "n":
                doxxer()
            else:
                doxxer()
        else:
            if platform.system() == "Linux":
                print(f'\n{Fore.GREEN}[~] Instalando IPlogger...')
                os.system(
                    "git clone https://github.com/Euronymou5/IPlogger && mv 'IPlogger' tools/"
                )
                print('\n[~] IPlogger instalado con exito.')
                time.sleep(2)
                doxxer()
            else:
                print(
                    f'\n{Fore.RED}[!] IPlogger no esta disponible para tu sistema operativo.'
                )
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
        doxxer()
