from os import system
from time import sleep
def logo():
    system('clear')
    print("""\033[1;31m
___  __   __        __     __  ___ ___      
 |  /  \ /  \ |    /__`     / |__   |  |__| 
 |  \__/ \__/ |___ .__/    /_ |___  |  |  | 
          Created By: Z-BL4CX-H4T                           """)
def menu():
    print("""
\033[1;31m1. \033[1;37mSTRANGE-TOOLS
\033[1;31m2. \033[1;37mDD0OS
\033[1;31m3. \033[1;37mEXIT
""")

    pil = input("ENTER YOUR CHOICES: \033[1;31m ")
    if pil =="1":
           sleep(2)
           system('clear')
           system('python3 STRANGE-TOOLS.py')
    if pil =="2":
           sleep(2)
           system('clear')
           print('\033[1;32m')
           system('figlet DD0OS')
           system('python3 DD0OS.py')
    if pil =="3":
           system('clear')
           system('python3 main.py')
logo()
menu()
