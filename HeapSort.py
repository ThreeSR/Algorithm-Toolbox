def heapify(arr,n,i):
    # n = len(arr) heap construction
    leftchild = 2*i + 1 # i starts with zero in python
    rightchild = 2*i + 2
    
    largest = i
    # maxheap
    if leftchild < n and arr[i] < arr[leftchild]:
        largest = leftchild
    if rightchild < n and arr[largest] < arr[rightchild]:# a little bit tricky
        largest = rightchild
    if i != largest:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr,n,largest)
    return arr


def heapsort(arr):
    n = len(arr)
    for i in range(n-1,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr,i,0)
    return arr
    
arr = list(map(int,input().split()))
arr2 = heapsort(arr)
for i in range(0,len(arr2)):
    print(arr2[i],end = ' ')
#print(heapsort(arr)) # print a list not numbers
    
    
    
    