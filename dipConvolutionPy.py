# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 11:51:14 2018
进行卷积训练;2018伊始，图像的卷积学习 convolve convolution
@author: Ricardolcf
"""


def convoluPy(img=""):
    import numpy as np
    from PIL import Image
    import cv2
    #robert=np.array([[0,1],[-1,0]])
    sobelHx=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    #sobelHy=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    
    if (img==""):
        img="D:/教学课件及学习资料/地空专业课/RS图像处理原理/broomConv.bmp"
    simg=Image.open(img)
    aimg=simg.convert("L")
    #print(aimg.mode)
    img_a=np.array(aimg)
    #img_b=np.array(aimg)
    #print(img_a)
    #im_t_P = Image.fromarray(img_a)
    #im_t_P.show()
    
    #不用np的高级特性，来两个for循环
    #M=img_a.shape[0]  #M对应x，N对应y
    #N=img_a.shape[1]
    #for x in range(1,M-1):#x==M-1时对应最后的元素
        #for y in range(1,N-1):
            #img_b[x][y]=abs(img_a[x][y]-img_a[x+1][y+1])+abs(img_a[x+1][y]-img_a[x][y+1])
    res=cv2.filter2D(img_a,-1,sobelHx)
    #print(res)
    
    im_t_PIL = Image.fromarray(res)
    im_t_PIL.show()

'''
随后深入学习：http://blog.csdn.net/zouxy09/article/details/49080029
http://www.cnblogs.com/youmuchen/p/6724780.html
'''

if(__name__=="__main__"):
    #img=""
    convoluPy()
    