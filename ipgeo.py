import ipinfo     
import subprocess
import sys
import io 
import os

handler = ipinfo.getHandler()
details = handler.getDetails() 
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


print(r"""
 ______  _______          ______   ________   ______         ________  _______    ______    ______   __    __  ________  _______  
/      |/       \        /      \ /        | /      \       /        |/       \  /      \  /      \ /  |  /  |/        |/       \ 
$$$$$$/ $$$$$$$  |      /$$$$$$  |$$$$$$$$/ /$$$$$$  |      $$$$$$$$/ $$$$$$$  |/$$$$$$  |/$$$$$$  |$$ | /$$/ $$$$$$$$/ $$$$$$$  |
  $$ |  $$ |__$$ |      $$ | _$$/ $$ |__    $$ |  $$ |         $$ |   $$ |__$$ |$$ |__$$ |$$ |  $$/ $$ |/$$/  $$ |__    $$ |__$$ |
  $$ |  $$    $$/       $$ |/    |$$    |   $$ |  $$ |         $$ |   $$    $$< $$    $$ |$$ |      $$  $$<   $$    |   $$    $$< 
  $$ |  $$$$$$$/        $$ |$$$$ |$$$$$/    $$ |  $$ |         $$ |   $$$$$$$  |$$$$$$$$ |$$ |   __ $$$$$  \  $$$$$/    $$$$$$$  |
 _$$ |_ $$ |            $$ \__$$ |$$ |_____ $$ \__$$ |         $$ |   $$ |  $$ |$$ |  $$ |$$ \__/  |$$ |$$  \ $$ |_____ $$ |  $$ |
/ $$   |$$ |            $$    $$/ $$       |$$    $$/          $$ |   $$ |  $$ |$$ |  $$ |$$    $$/ $$ | $$  |$$       |$$ |  $$ |
$$$$$$/ $$/              $$$$$$/  $$$$$$$$/  $$$$$$/           $$/    $$/   $$/ $$/   $$/  $$$$$$/  $$/   $$/ $$$$$$$$/ $$/   $$/ 
""")

print("\033[1;33m ================================================================================================== \033[1;33m")
    
print('''\033[0;34m Created by: AlexRods9581''')
print('''\033[0;34m Github: https://github.com/AlexRodrigues9581''')

print("\033[1;33m ================================================================================================== \033[1;33m")


def menu():
    
    print("1 - Geolocate my own IP \n2 - Geolocate IP \n3 - Exit ")
    op = input("Select an option:")
    
    if op == "1":
        own_ip()
        
    if op == "2":
        ip()
        
    if op == "3":
        exit
    
def own_ip():
    handler = ipinfo.getHandler()
    details = handler.getDetails()
    for key, value in details.all.items():
        print(f"\033[0;34m{key}: {value}\033[0m")

def ip():
    ip = input("Enter the IP to be geolocated:")
    handler = ipinfo.getHandler()
    details = handler.getDetails(ip)
    for key, value in details.all.items():
        print(f"\033[0;34m{key}: {value}\033[0m")


if __name__ == "__main__":
    menu()
    
    
    