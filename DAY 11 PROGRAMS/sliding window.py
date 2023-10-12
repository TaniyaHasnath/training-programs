def sliding_window(arr,k):
    sldiding_window=0
    i,j=0,k-1
    while j<len(arr):
        if i==0:
            sliding_window=sum(arr[i:j+1])
            ps=sliding_window
        else:
            cs=ps-arr[i-1]+arr[j]
            sliding_window=max(sliding_window,cs)
            ps=cs
        i+=1
        j+=1
    return  sliding_window
print(sliding_window([-3,20,3,-9,18,-45,23,67],3))