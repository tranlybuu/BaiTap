import string,random
import random
n=random.randint(50,101)
print("Số phần tử đã được random là số:",n)
array=[]
for i in range(n):
    R=dict()
    n=random.randrange(1,20)
    G=random.choice(string.ascii_uppercase)
    H=G+''.join(random.choice(string.ascii_lowercase) for i in range(n-1))
    R['name']=H
    A=random.randrange(1,100)
    R['age']=A
    array.append(R)
print(array)