# Cây thông noel
# Trần
# Lý 
# Bửu
# Just_For_Fun

from colorama import Fore, Back, Style, init
import time
import os

init()
size = 30
mess=["Hôm nay 25/12","Giáng sinh vui vẻ","Merry Christmas...!","(^o^)"]

def wait():
    time.sleep(0.5)

def wait2():
    time.sleep(1)

def clear():
    os.system('cls')

def intro(text):
    print("+{}+".format("".center(30, "=")))
    print("|                              |")
    print("|{}|".format(text.center(30, " ")))
    print("|                              |")
    print("+{}+".format("".center(30, "=")))

clear()

for text in mess:
    intro(text)
    wait2()
    clear()

for i in range(0, size-15):
    if i == 0:
        print(Fore.YELLOW + "★".center(size, " "))
        wait()
    elif i % 2 == 0 and i > 0:
        print(Fore.GREEN + ("*"*i).center(size, " "))
        wait()
    else:
        print(Fore.RED + ("^"*(i+1)).center(size, " "))
    
for i in range(3):
    print(Fore.WHITE + "||".center(size, " "))
    wait()
print("====".center(size, " "))

init(autoreset=True)
print(Back.RED + "Made by TLBuu".center(size, " "))
print()