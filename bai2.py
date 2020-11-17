def giaipt():
    print("Phương trình bậc nhất có dạng a*x+b=c")
    a=float(input("Nhập a: "))
    b=float(input("Nhập b: "))
    c=float(input("Nhập c: "))
    if a==0:
        print("Nhập sai rồi kìa")
    else:
        print("x =",(c-b)/a)

n=int(input("Nhập số lần lặp giải phương trình n = "))

print("Giải bằng For")
for i in range(n):
    giaipt()
print("Kết thúc For\n")

print("Giải bằng While")
while n>0:
    giaipt()
    n-=1
print("Kết thúc While")