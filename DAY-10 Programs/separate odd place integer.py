#separate odd place integer
n,k=map(int,input().split())
lst=[]
for i in range(n):
    lst.append(int(input()))
s,c=set(lst),0
for i in s:
    if lst.count(i)>=k:
        c+=1
print(c)
    
        