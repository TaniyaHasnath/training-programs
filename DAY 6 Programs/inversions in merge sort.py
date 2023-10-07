# inversions in python
l=[9,6,8,7]
c=0
for i in range(len(l)-1):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            c+=1
print(c)