# -*- coding: utf-8 -*-

'''
five-programming-problems-every-software-engineer-should-be-able-to-solve-in-less-than-1-hour
Solve them with Python
'''

#1,使用for循环、while循环和递归写出3个函数来计算给定数列的总和。
def sumListTway(way,nlst): #for & while
    if way==1:#没怎么用异常处理
        nlen=len(nlst)
        snlst=0
        for i in range(nlen):
            snlst+=nlst[i] #snlst=snlst+nlst[i]
        return snlst
    elif way==2:
        nlen=len(nlst)
        snlst=0
        i=0
        while i<nlen:  # i<len(nlst),不取等号
            snlst+=nlst[i]
            i+=1
    else:
        return sum(nlst)
    
def sumlstRec(nlst): #递归
    nlen=len(nlst)
    if nlen==1:
        return nlst[0] 
    else: #py没必要分奇偶
        return sumlstRec(nlst[0:nlen//2])+sumlstRec(nlst[nlen//2:])


#2,编写一个交错合并列表元素的函数。eg：给定的两个列表为[a，B，C]和[1，2，3]，函数返回[a，1，B，2，C，3]。
def interlaceList(nl,ml):
    nlen=len(nl)
    mlen=len(ml)
    newlst=[]
    if nlen==mlen:
        for i in range(0,nlen):
            newlst.append(nl[i])
            newlst.append(ml[i])
    else:
        #minNL=min(nlen,mlen)
        if nlen>mlen:#默认nlen<mlen
            nl,ml=ml,nl
            nlen,mlen=mlen,nlen #感觉比再nlen=len(nl)开销小
        for i in range(0,nlen):
            newlst.append(nl[i])
            newlst.append(ml[i])#先不考虑本题[1,'a']和['a',1]的不同
        newlst.extend(ml[nlen:])
    return newlst


#3,计算前N位斐波那契数的函数
def fib_loop(n): #递推法 O(n),还是通项法较优
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a #不返回所有值，要返回也简单


def fib_matr(n): #矩阵计算法：  O(log（n）)
    import numpy #矩阵推导参见 ‘经典练习汇.doc’
    return (numpy.matrix([[1, 1], [1, 0]]) ** (n - 1) * numpy.matrix([[1], [0]]))[0, 0]


#4,编写一个能将给定非负整数列表中的数字排列成最大数字的函数。例如，给定[50，2，1,9]，最大数字为95021。

def rangeMax(nlst):
    pass

#4.1，拆掉数组中的元素，可以得  95210
def rangeRealMax(nlst):# 4.1 
    numberlst=[]
    for item in nlst:
        ilen=len(str(item))
        if ilen==1:
            numberlst.append(item)
        else:
            for k in str(item):
                numberlst.append(int(k))
    lsum=0
    numberlst.sort(reverse=True)
    numlen=len(numberlst)
    #最终结果可以用str求也可以循环数字
    for i in range(numlen):
        lsum+=numberlst[i]*(10**(numlen-i-1))
    return lsum


#5,编写一个在1，2，…，9（顺序不能变）数字之间插入+或-或什么都不插入，使得计算结果总是100的程序，并输出所有的可能性。例如：1 + 2 + 34 – 5 + 67 – 8 + 9 = 100。
def getHundred():
    pass
#暴力法：八个for循环
def ThreeTimes():
    pass

if __name__ == '__main__':
    rangeRealMax(range(1,6))
