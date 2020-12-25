import csv

with open('high_temps.csv','w') as f:
    w = csv.writer(f)
    w.writerows(data.items())