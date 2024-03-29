function install() {
   clear
   echo -e "\033[32m[~] Actualizando paquetes..."
   apt update
  

   sleep 3
   which python3 > /dev/null 2>&1
   if [ "$?" -eq "0" ]; then
   echo -e "\033[32m\n[~] Python3 ya esta instalado."
   else
   echo -e "\033[31m\n[!] Python3 no esta instalado."
   sleep 2
   echo -e "\033[32m\n[~] Instalando python3..."
   apt install python3 -y
   fi
   
   sleep 3
   which pip3 > /dev/null 2>&1
   if [ "$?" -eq "0" ]; then
   echo -e "\033[32m\n[~] pip3 ya esta instalado."
   else
   echo -e "\033[31m\n[!] pip3 no esta instalado."
   sleep 2
   echo -e "\033[32m\n[~] Instalando pip3..."
   wget https://bootstrap.pypa.io/get-pip.py
   python3 get-pip.py
   rm -rf get-pip.py
   fi

   sleep 3
   which nmap > /dev/null 2>&1
   if [ "$?" -eq "0" ]; then
   echo -e "\033[32m\n[~] Nmap ya esta instalado."
   else
   echo -e "\033[32m\n[!] Nmap no esta instalado."
   sleep 2
   echo -e "\033[32m\n[~] Instalando nmap..."
   git clone https://github.com/nmap/nmap.git
   chmod -R 755 nmap && cd nmap && ./configure && make && make install
   fi
   
   echo -e "\033[32m\n[~] Instalando requerimientos..."
   pip3 install -r requirements.txt
   
   echo -e "\n\033[32m[✔] Instalacion completada."
   echo -e "\n[~] Utiliza el comando: python3 fuckyou.py para iniciar la herramienta."
}

install
