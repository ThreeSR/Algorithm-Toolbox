def bin_search(data,element):
    l = 0
    r = len(data) - 1
    while(l<=r):
        mid = (l+r) // 2
        if (element == data[mid]):
            return mid
        if (element > data[mid]):
            l = mid + 1
        else:
            r = mid - 1
    return -1

data1 = list(map(int,input().split()))
data2 = list(map(int,input().split()))

n = data1[0]
data = data1[1:]
#data.sort(reverse = 1)
m = data2[0]
Search = data2[1:]
record = []
for i in range(m):
    if (bin_search(data,Search[i])==-1):
        record.append(-1)
    else:
        record.append(bin_search(data,Search[i]))

for i in range(m):
    print(record[i],end=' ')
