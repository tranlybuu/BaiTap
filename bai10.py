list2 = [({'name': 'Peter', 'age':2}, {'name': 'John', 'age':21}), 
         ({'name': 'Mary', 'age':2}, {'name': 'Trandanpro', 'age':21}), 
         ({'name': 'Nam', 'age':2}, {'name': 'Hung', 'age':21}), 
         ({'name': 'Mai', 'age':2}, {'name': 'Loan', 'age':21})]

print("List gồm {} phần tử\n".format(len(list2)))
for i in range(len(list2)):
    length=len(list2[i])
    print("Phần tử thứ {} có {} phần tử con:".format(i+1,length))
    check=list(enumerate(list2[i]))
    for v in check:
        print(v)