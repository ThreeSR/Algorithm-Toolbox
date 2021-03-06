# Reference: Grokking Algorithms: An illustrated guide for programmers and other curious people
# Aditya Bhargava

def quicksort(S):
    # Baseline 
    if len(S) < 2:
        return S
    else:
        pivot = S[0]
        greater = [i for i in S[1:] if i > pivot]
        less = [i for i in S[1:] if i < pivot]
        equal = [i for i in S[1:] if i == pivot]
        return quicksort(less) + equal + [pivot] + quicksort(greater)

#n = int(input())
S = list(map(int,input().split()))
S = quicksort(S)
for i in range(len(S)):
    print(S[i],end = ' ')
