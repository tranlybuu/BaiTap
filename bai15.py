import os
 
path = input("Nhập đường dẫn tới thư mục: ")
 
#di chuyển đến thư mục đích
os.chdir(path)
 
#tạo một thưu mục mới có tên là test
file=open("test.txt","w",encoding="utf-8")
str=input("Nhập nội dung trong file test.txt: ")
file.write(str)
file.close()