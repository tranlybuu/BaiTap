import time
import os

while True:
    check=input("Bạn có muốn tắt máy không? (Yes/No)  ")
    if "Yes" == check or "yes" == check:
        break
    elif "No" == check or "no" == check:
        time.sleep(30)
    else:
        print("Trả lời YES hoặc NO thôi mà cũng nhập sai. Hãy nhập lại")
        time.sleep(3)
    os.system('cls')
end=input("ENTER để kết thúc")