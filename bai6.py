import random

array=[]
n=int(input("Nhập số phần tử muốn tạo trong list: "))

#Tạo một List gồm các số thực (tạo ngẫu nhiên bằng hàm random với số lượng phần tử của list là số n nhập vào từ bàn phím)
for i in range(n):
    array.append(int(random.randrange(-10000,10000,1)))
print(array)

#Hãy tìm phần tử có giá trị nhỏ nhất của List và in ra màn hình
array.sort()
print(array[0])