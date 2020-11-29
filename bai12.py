import string,random
R=dict()
n=random.randrange(1,20)
G=random.choice(string.ascii_uppercase)
H=G+''.join(random.choice(string.ascii_lowercase) for i in range(n-1))
R['name']=H
A=random.randrange(1,100)
R['age']=A
print("Random Dictionary: ",R)