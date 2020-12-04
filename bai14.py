import os
"""print("Các hàm cơ bản của thư viện OS\n",dir(os))
print("Các tập tin trong ổ C:\n",os.listdir("C:\\"))"""
path="D:"
"""sửa D thành C"""
file=[]
for r,d,f in os.walk(path):
    for sfile in f:
        file.append(os.path.join(r,sfile))
for i in file:
    print(i)