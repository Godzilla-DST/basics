###__libarary__###

import os
import time
import name 
name.name()

###__variable__###

r = "\033[1;31m"
g = "\033[1;32m"
b = "\033[1;34m"
loop = True
t5 = time.sleep(5)
t2 = time.sleep(2)
t_4 = time.sleep(.4)
clear = os.system("clear")

###__functions__###

def loading() :
     for x in range(10) :
        print(" \033[1;34m loading "," \033[1;31m ########################",end="\r")
        time.sleep(.07)
        print(" \033[1;34m loading "," \033[1;32m ###""\033[1;31m#####################",end="\r")
        time.sleep(.07)
        print(" \033[1;34m loading "," \033[1;31m ###""\033[1;32m###""\033[1;31m##################",end="\r")
        time.sleep(.07)
        print(" \033[1;34m loading "," \033[1;31m ######""\033[1;32m###""\033[1;31m###############",end="\r")
        time.sleep(.07)
        print(" \033[1;34m loading "," \033[1;31m #########""\033[1;32m###""\033[1;31m############",end="\r")
        time.sleep(.07)
        print(" \033[1;34m loading "," \033[1;31m ############""\033[1;32m###""\033[1;31m#########",end="\r")
        time.sleep(.07)
        print(" \033[1;34m loading "," \033[1;31m ###############""\033[1;31m###""\033[1;31m######",end="\r")
        time.sleep(.07)
        print(" \033[1;34m loading "," \033[1;31m ##################""\033[1;32m###""\033[1;31m###",end="\r")
        time.sleep(.07)
        print(" \033[1;34m loading "," \033[1;31m #####################""\033[1;32m###",end="\r")
        time.sleep(.07)
        print("                                                                                ",end="\r")

######################################################################################################################

def design() :
    clear
    print(g,"                          _")
    print(g,"                         | |")
    print(g,"                         | |")
    print(g,"                         | |")
    print(g,"                         | |")
    print(g,"                         | |")
    print(g,"                         | |")
    print(g,"_________________________| |____________________________")
    print(g,"|    ______________      | |       _______________     |")
    print(g,"|   |              |     | |      |               |    |")
    print(g,"|   |  (0) = exit  |     | |      | (1) = install |    |")
    print(g,"|   |              |     | |      |               |    |")
    print(g,"|   | DST GODZILLA |     | |      |  DST GODZILLA |    |")
    print(g,"|   |______________|     | |      |_______________|    |")
    print(g,"|                        | |                           |")
    print(g,"|________________________|_|___________________________|")
    choose = input("choose number =======>>> ")

########################################################################################################################



###__code__###

print(g,"                          _")
print(g,"                         | |")
print(g,"                         | |")
print(g,"                         | |")
print(g,"                         | |")
print(g,"                         | |")
print(g,"                         | |")
print(g,"_________________________| |____________________________")
print(g,"|    ______________      | |       _______________     |")
print(g,"|   |              |     | |      |               |    |")
print(g,"|   |  (0) = exit  |     | |      | (1) = install |    |")
print(g,"|   |              |     | |      |               |    |")
print(g,"|   | DST GODZILLA |     | |      |  DST GODZILLA |    |")
print(g,"|   |______________|     | |      |_______________|    |")
print(g,"|                        | |                           |")
print(g,"|________________________|_|___________________________|")
choose =input("choose number =======>>> ")

while loop:
    if  choose == "1" :
        
        print(r,"[+]  installing be take a long time ")
        print(r,"[+]  USE WIFI ONLY")
        t2
        
        con = input("do you want to continue y/n ======>>> ")
        if con == "y" :
            os.system("apt update -y")
            os.system("apt upgrade -y")
            os.system("pkg update -y")
            os.system("pkg upgrade -y")
            os.system("termux-setup-storage -y")
            os.system("apt-get update -y")
            os.system("apt-get upgrade -y")
            os.system("apt install php -y")
            os.system("apt install python -y")
            os.system("apt install python2 -y")
            os.system("apt install git -y")
            os.system("gem install golang -y")
            os.system("gem install host -y")
            os.system("apt install nano -y")
            os.system("gem install havij -y")
            os.system("gem install hydra -y")
            os.system("gem install wireshark -y")
            os.system("pkg install figlet -y")
            os.system("gem install wget -y")
            os.system("pkg install cowsay -y")
            os.system("pkg install toilet -y")
            os.system("pkg install ruby -y")
            os.system("gem install help -y")
            os.system("gem install lolcat -y")
            os.system("pkg install curl -y")
            os.system("gem install wgetrc -y")
            os.system("pkg install unzip -y")
            os.system("gem install openssh -y")
            os.system("pkg install tor -y")
            os.system("pkg install zip -y")
            os.system("pkg install net-tools -y")
            os.system("pkg install unrar -y")
            os.system("pkg install clang -y")
            os.system("pkg install w3m -y")
            os.system("pkg install proot -y")
            os.system("pip2 install wegt -y")
            os.system("pip2 install requests -y")
            os.system("pkg install sl -y")
            os.system("pkg install unstable-repo")
            os.system("pkg install x11-repo")
            os.system("pkg install root-repo")
            os.system("pkg install proot")
            os.system("gem install bundle")
            os.system("gem install bundler")
            os.system("pip install --upgrade pip")
            os.system("pip install pip")
            os.system("pip install --upgrade pip")
            os.system("pip2 install pip")
            os.system("pip3 install pip")
            os.system("apt update && apt upgrade && pkg update && pkg upgrade -y")
            t2
            loading()
            os.system("clear")
            print ("install done :)")
            t2
            os.system("clear")
            design()
        elif con == "n" :
            design()
        else :
            con = input("do you want to continue y/n ======>>> ")
    elif choose == "0" :
        os.system("exit")
    else :
        choose =input("choose number =======>>> ")
