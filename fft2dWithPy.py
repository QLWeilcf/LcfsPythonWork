# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 22:06:41 2017
二维傅里叶变换
@author: Ricardolcf
"""

from PIL import Image
import numpy as np
from matplotlib import pyplot as plt


def dft2d(mnx): #输入mnx为二维np.array()
    M=mnx.shape[0]  #M对应x，N对应y
    N=mnx.shape[1]
    lst=np.ones((M,N),dtype=complex) #保存结果的ndarray()
    #lst = np.ones((M, N),dtype=float)
    for u in range(0,M):
        for v in range(0,N):
            k=0
            for x in range(0,M):
                for y in range(0,N):
                    #k = mnx[x][y] * np.cos(2 * np.pi * (u * x / M + v * y / N)) + k #不要求虚部时
                    k=mnx[x][y]*np.exp(-2j * np.pi *(u*x/M+v*y/N))+k

            lst[u,v]=k

    return lst

def idft2d(mnx):  #逆变换
    M=mnx.shape[0]
    N=mnx.shape[1]
    tf=np.ones((M,N),dtype=complex) #保存结果的数组
    for x in range(0,M):
        for y in range(0,N):
            k=0
            for u in range(0,M):
                for v in range(0,N):
                    k=mnx[u][v]*np.exp(2j * np.pi *(u*x/M+v*y/N))+k

            tf[x,y]=k/(M*N)
    
    return tf

def mnxtoCompx(mnx): #构建行列数和mnx相等的复数数组
    M = mnx.shape[0]  # M对应x，N对应y
    N = mnx.shape[1]  
    mnew = np.zeros((M, N), dtype=complex)
    for v in range(0,M):
        for u in range(0,N):
            mnew[v][u]=mnx[v][u]
    #print(mnew.dtype)
    return mnew


def fft2d(mnx): #二维快速傅里叶变换
    M = mnx.shape[0]  # M对应x，N对应y
    N = mnx.shape[1]  #默认M==N

    if (M % 2 > 0 or N % 2 > 0 ):# or M!=N
        print("input pic not reasonable now")
        return

    c=int(np.log2(M))  #分解级数

    mnew = mnxtoCompx(mnx) #构建行列数和mnx相等的复数数组,直接对mnx处理不方便比较且不好debug

    t=np.ones((1,1),dtype=complex)[0][0]
    for i in range(0,M):   #时域抽取
        c = int(np.log2(N)) #进行逆序重排
        kn=N//2
        for u in range(1,N-1):
            if (u<kn):
                mnew[i][kn],mnew[i][u]=mnew[i][u],mnew[i][kn]
            lw=N//2
            while (lw<=kn):
                kn=kn-lw
                lw=lw//2
            kn+=lw

        for j in range(1, c + 1):  #43
            la = 2 ** j  #第j级每个分组所含节点数
            lb = la // 2 #第j级每个分组所含碟形单元数
            for k in range(1, lb + 1): #碟形运算
                rig = (k - 1) * (2 ** (c - j))
                for v in range(k - 1, N-1, la):
                    lc = v + lb
                    tc = mnew[i][lc]*np.exp(-2j * np.pi *rig/ N)
                    #tc = mnew[lc][i] * np.exp(-2j * np.pi / M) ** rig
                    mnew[i][lc]=mnew[i][v]-tc
                    mnew[i][v]=mnew[i][v]+tc

    for i in range(0,N):
        kn = M // 2
        for u in range(1, M - 1):
            if (u < kn):
                mnew[kn][i], mnew[u][i] = mnew[u][i], mnew[kn][i]
            lw = M // 2
            while (lw <= kn):   #
                kn -= lw
                lw = lw // 2
            kn += lw

        for j in range(1, c + 1):  #
            la = 2 ** j
            lb = la // 2
            for k in range(1, lb + 1):  # 碟形运算
                rig = (k - 1) * (2 ** (c - j))
                for v in range(k - 1, M-1, la):
                    lc = v + lb
                    tc = mnew[lc][i] * np.exp(-2j * np.pi * rig / M)
                    mnew[lc][i] = mnew[v][i] - tc
                    mnew[v][i] = mnew[v][i] + tc

    return mnew


def ifft2d(mnx):  #快速逆运算
    M = mnx.shape[0]  # M对应x，N对应y
    N = mnx.shape[1]  # 默认M==N

    if (M % 2 > 0 or N % 2 > 0 ):#or N != M
        print("2**")
        return
    c=int(np.log2(M))
    mnw = np.zeros((1, 1), dtype=complex)
    tp = mnw[0][0]+M

    for i in range(0,N):  #逐列

        for v in range(0,M):
            mnx[v][i]=mnx[v][i]/tp  #处理复数的部分并除1/M
        for u in range(1, c+1):
            la=2**(c+1-u)
            lb=la//2

            for k in range(1, lb + 1):  # 碟形运算
                rig = (k - 1) * (2 ** (u - 1))
                for v in range(k - 1, M-1, la):
                    lc = v + lb
                    tc=mnx[v][i]+mnx[lc][i];
                    mnx[lc][i]=(mnx[v][i]-mnx[lc][i])* np.exp(-2j * np.pi * rig / M)
                    mnx[v][i]=tc

        kn = M // 2
        for h in range(1,M-1):
            if (h<kn):
                mnx[kn][i],mnx[h][i]=mnx[h][i],mnx[kn][i]

            lw=M//2
            while (lw <= kn):   #
                kn -= lw
                lw = lw // 2
            kn += lw
        for s in range(1, M // 2):
            mnx[M - s][i], mnx[s][i] = mnx[s][i], mnx[M - s][i]

    for i in range(0, M):  #逐行

        kn = M // 2
        for v in range(0, M):
            mnx[i][v] = mnx[i][v] / tp  # 处理复数的部分并除1/M

        for u in range(1, c + 1):
            la = 2 ** (c + 1 - u)
            lb = la // 2

            for k in range(1, lb + 1):  # 碟形运算
                rig = (k - 1) * (2 ** (u - 1))
                for v in range(k - 1, N - 1, la):
                    lc = v + lb
                    tc = mnx[i][v] + mnx[i][lc];
                    mnx[i][lc] = (mnx[i][v] - mnx[i][lc]) * np.exp(-2j * np.pi * rig / N)
                    mnx[i][v] = tc

        for h in range(1, N-1):
            if (h < kn):
                mnx[i][kn], mnx[i][h] = mnx[i][h], mnx[i][kn]

            lw = N // 2
            while (lw <= kn):  #
                kn -= lw
                lw = lw // 2
            kn += lw
        for s in range(1, M // 2):
            mnx[i][M - s], mnx[i][s] = mnx[i][s], mnx[i][M - s]
    return mnx


def testFFT2d():
    from datetime import datetime
    st=datetime.now()
    simg = Image.open("./spydyhomecoming512x512.bmp")
    imgarr = np.array(simg)
    print('spydyhomecoming512x512')
    #print(imgarr)
    #dft_rsl=dft2d(imgarr)
    np_rsl=np.fft.fft2(imgarr)
    #print('dft:')
    #print(dft_rsl)
    #print(np.allclose(dft_rsl,np_rsl))#对比普通傅里叶变换的结果

    fft_rsl=fft2d(imgarr)  #快速傅里叶变换部分
    print(np.allclose(fft_rsl, np_rsl))

    print(np.allclose(np.fft.ifft2(fft_rsl),ifft2d(fft_rsl)))
    print(datetime.now()-st)
    #print(ifft2d(fft_rsl))



if __name__ == '__main__':
	testFFT2d()
	
	
'''
## 参考资料：

[FastFourierTransform Wiki](https://en.wikipedia.org/wiki/Fast_Fourier_transform)
[Numpy fft2](https://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.fft2.html#numpy.fft.fft2)
[理解快速傅里叶变换](http://blog.jobbole.com/58246/)
'''




