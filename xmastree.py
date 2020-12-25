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
mess=["Hôm nay 25/12","Gần kết thúc năm 2020","Chúc mọi người giáng sinh vui vẻ","Merry Christmas...!","(^o^)"]

def wait():
    time.sleep(0.5)

def wait2():
    time.sleep(1)

def clear():
    os.system('cls')

def intro(text):
    print("+{}+".format("".center(37, "=")))
    print("|                                     |")
    print("|{}|".format(text.center(37, " ")))
    print("|                                     |")
    print("+{}+".format("".center(37, "=")))

clear()

for text in mess:
    intro(text)
    wait2()
    clear()

for i in range(0, size):
    if i == 0:
        print(Fore.YELLOW + "★".center(size+4, " "))
        wait()
    elif i % 2 == 0 and i > 0:
        print(Fore.GREEN + ("*"*i).center(size+4, " "))
        wait()
    else:
        print(Fore.RED + ("^"*(i+1)).center(size+4, " "))
    
for i in range(5):
    print(Fore.GREEN + "||".center(size+4, " "))
    wait()
print("====".center(size+4, " "))

init(autoreset=True)
print(Back.RED + "Made by TLBuu".center(size+4, " "))