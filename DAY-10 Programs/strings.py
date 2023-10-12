def demo(s): # strings#2,5,1,4,3,2,7,8
    los=s.split(',')
    idxpof=los.index('4')
    idxpos=los.index('7')
    n1,n2=0,''
    for i in los[:idxpof]+los[idxpos+1:]:
        n1+=int(i)
    for i in los[idxpof:idxpos+1]:
        n2+=i
    return(n1+int(n2))
s=input()
if __name__=='__main__':
     print(demo(s))