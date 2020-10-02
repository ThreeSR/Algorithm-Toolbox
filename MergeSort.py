def mergesort(seq):
    if len(seq) <= 1:
        return seq
    mid = len(seq)//2  
    
    left = mergesort(seq[:mid])
    right = mergesort(seq[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []  
    i = 0  
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

seq = [5,3,0,6,1,4]
print(seq)
result = mergesort(seq)
print(result)

