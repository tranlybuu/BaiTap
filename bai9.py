#Bài 1
"""
import numpy as np
arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr2=np.array([[3,2,1],[6,5,4],[9,8,7]])
tong=arr1+arr2
tich=arr1.dot(arr2)
chuyen_vi=tong.transpose()
print("Tổng 2 ma trận arr1 và arr2 là:\n",tong)
print("\nTích 2 ma trận arr1 và arr2 là:\n",tich)
print("\nMA trận chuyển vị của tổng 2 ma trận arr1 và arr2 là:\n",chuyen_vi)
"""

#Bài 2
"""import pandas as pd
import io
import requests
import urllib2
import json

print("Đọc csv từ máy tính")
test = pd.read_csv('./test.csv', encoding='utf-8', header=None, sep=',')
print(test.head(10))

print("\nĐọc csv từ web")
url="https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
s=requests.get(url).content
c=pd.read_csv(io.StringIO(s.decode('utf-8')))
print(c.head(5))

print("\nĐọc Json từ web")
response = urllib2.urlopen('https://api.github.com/users/voduytuan/repos')
data = json.load(response)
print(data)"""

#Bài 3

import matplotlib.pyplot as plt
ex=[0,1,2,6,11,8,15]
week=[1,2,3,4,5,6,7]
deg=[40,61,26,73,25,37,48,96]
mon=[2,5,6,2,7,8,3,2]
value1 = [82,76,24,40,67,62,75,78,71,32,98,89,78,67,72,82,87,66,56,52]
value2=[62,5,91,25,36,32,96,95,3,90,95,32,27,55,100,15,71,11,37,21]
value3=[23,89,12,78,72,89,25,69,68,86,19,49,15,16,16,75,65,31,25,52]
value4=[59,73,70,16,81,61,88,98,10,87,29,72,16,23,72,88,78,99,75,30]

#Vẽ đồ thị hình bar
plt.bar(week,ex)

#Vẽ đồ thị hình line
plt.plot(mon,deg,marker='.',markersize=10)

#Vẽ đồ thị hình box
box_plot_data=[value1,value2,value3,value4]
plt.boxplot(box_plot_data)

plt.show()