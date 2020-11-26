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

import pandas as pd
s = pd.Series([0,1,2,3])
print(s)