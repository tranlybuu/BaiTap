import random
n=random.randint(50,1001)
print("Số phần tử đã được random là số:",n)
integer_array=[]
float_array=[]
for i in range(n):
    integer_array.append(random.randint(-1000,1001))
    float_array.append(random.uniform(-1000.0,1000.0))
print("\nList số nguyên là:\n",integer_array)
print("\nList số thực là:\n",float_array)