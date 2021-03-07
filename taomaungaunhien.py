import pandas as pd
import random


dfdata = pd.read_csv('D:\\OffCode\\danhsachlop.csv')
#print(dfdata)
random_selected = dfdata.sample(n=7)
#print(random_selected)
random_selected.to_csv('D:\\OffCode\\random7sv.csv')