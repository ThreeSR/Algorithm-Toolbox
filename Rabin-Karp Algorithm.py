# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 14:54:14 2020

@author: lneovo
"""

def search(txt,pat,q):
    # 参数初始化
    t = 0 # hash value for txt
    p = 0 # hash value for pat
    d = 256 # number of elements in ASCII
    M = len(pat)
    N = len(txt)
    h = 1 #最高次幂数值，这个值被赋为1，后面循环就要少一次
    index = [] # store the index for found pattern in text

    for i in range(M-1):# 因为一开始 h=1，所以最后的循环要少一次
        h = (h*d)%q # hash value 的最高次幂 取模可以降低运算开销
    for i in range(M): # 初始化p和t对应原文中的哈希值
        p = (p*d + ord(pat[i]))%q # hash value in pattern
        t = (t*d + ord(txt[i]))%q # hash value in text. our goal achieved if t = p
    for i in range(N-M+1):        # 循环N-M+1不是N-M，是因为N-M不能检测到最后一个字符   
            if p == t:
                # prevent fake result, need further exam
                for j in range(M): # 防止伪命中，逐个检测
                    if pat[j] != txt[i+j]:
                       break
                    if j == M-1: # 代表检测到了最后，是真结果，不是伪命中
                       index.append(i)
            if i < N-M: # 上面为了检测到最后一个点，i可以取到N-M，但对于移位运算，txt会out of range。
            # 此外，如果检测到了最后一个字符，代表检测到此结束，t不用再移位更新，因此i保证txt不会out of range，
            # 并且能保证最后一次t的更新够用就行。所以取i<N-M,可以匹配。这有点啰嗦，但此处i取值确实与大循环略有不同。
            # shift operation                 
                t = (d*(t-h*ord(txt[i])) + ord(txt[i+M]))%q           
                if t < 0: # 防止t为负数，必要时把t加回正数
                    t = t + q             
    return index
# drive code         
txt = "Geeks for Geeks"
pat = "eekd"
q = 101  # q可以取值大一些，理论上来说，q越大，伪命中概率越低，需要check的次数少，但也不是q越大越好
result = search(txt,pat,q)
if len(result) == 0:
    print("Not Found")
else:
    print("Pattern is found in Text, their indexes are:" + str(result))