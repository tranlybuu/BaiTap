import os
print("Các hàm cơ bản của thư viện OS\n",dir(os))
print("Các tập tin trong ổ C:\n",os.listdir("C:\\"))
path="C:"

file=[]
arr1=[]
arr2=[]
for r,d,f in os.walk(path):
    for sfile in f:
        file.append(os.path.join(r,sfile))
    if d!=[]:
        arr1.append(d)
    if f!=[]:
        arr2.append(f)
print("\n\nTất cả tập tin và thư mục con trực tiếp của thư mục gốc ổ đĩa C:")
for i in file:
    print(i)
print("\n\nDanh sách thư mục:")
for i in arr1:
    print(i)
print("\n\nDanh sách tập tin:")
for i in arr2:
    print(i)