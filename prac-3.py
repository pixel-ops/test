a = ["eat","tea","tan","ate","nat","bat"]
# a = [""]
# a = ["a"]
mylist = set()

for i in range(len(a)):
    col = []
    for j in range(0,len(a)):
        if sorted(a[i]) == sorted(a[j]):
           col.append(a[j]) 
    mylist.add(tuple(col))



b = list(mylist)
res = [list(i) for i in b]
print(res)

