import math
#Tạo một List gồm cấc số thực (có thể tạo bằng tay hoặc ngẫu nhiên) (lưu ý: nằm ngoài vòng lặp)
array=[8,3,6,0,1,7,4,2]

#Thực hiện lặp truy xuất đến từng phần tử trong List và in giá trị của từng phần tử ra màn hình
print("Các phần tử trong list là:")
for i in array:
    print(i)

#Thực hiện lặp truy xuất đến từng phần tử trong List và thực hiện tính logarith của từng phần tử và in giá trị đó ra màn hình
print("\nTính log của các giá trị trong list:")
for i in array:
    if i<=0:
        print("Số {} không thể tính log".format(i))
    else:
        print("Giá trị log của số {} là {}".format(i,math.log(i)))