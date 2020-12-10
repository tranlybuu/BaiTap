import os,random
import string
t=input('Nhập tên thư mục: ')
path='C:\\' 
os.chdir(path)
os.mkdir(t)
file_name = input("Nhập tên file dữ liệu: ")
n=int(input("Nhập dung lượng 1MB-1024MB của thư mục: "))
for i in range(n):
    path1 = path + t
    os.chdir(path1)
    file=open(file_name + " lần thứ "+ str(i+1) + '.txt','w+')
    file.seek(1024*1000-1)
    file.write("random.choice(string.ascii_lowercase)")
if file.seek(0):
    os.remove(file)
file.close()
