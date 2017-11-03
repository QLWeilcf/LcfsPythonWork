# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 08:12:24 2017

@author: Ricardolcf

角点检测 Harris算法
还有需要完善的东西
"""

from PIL import Image,ImageDraw
import numpy as np

def harrisPy(img,thsd): # 输入为图片和阈值
    if (img.mode=='RGB'): #只用一个通道
        img=img.convert("L")
        #img.show()
    imgarr=np.array(img) #转为np数组
    Ix,Iy=np.gradient(imgarr)  #求两个方向的梯度
    Ix2=Ix*Ix
    Iy2=Iy*Iy
    Ixy=Ix*Iy
    M=imgarr.shape[0]  #M对应x，N对应y
    N=imgarr.shape[1]
    k=0.04
    cornerArr=[]
    for i in range(2,M-2): #逐个像素点判断
        for j in range(2,N-2):
            wdix2=Ix2[i-2:i+3,j-2:j+3] #移动窗口
            wdiy2=Iy2[i-2:i+3,j-2:j+3]
            wdixy=Ixy[i-2:i+3,j-2:j+3]
            
            sumx2=wdix2.sum()  #求和 sum(wdix2)结果不对
            sumy2=wdiy2.sum()
            sumxy=wdixy.sum()
            
            detR=sumx2*sumy2-sumxy*sumxy #求det
            trcR=sumx2+sumy2  #按照算法写的，感觉单个方向梯度变化很大也会使得R很大，这不应该呀
            R=detR-k*(trcR**2)   #根据一般的Harris算法求R，一种优化算法为(Ix2*Iy2-Ixy)/(Ix2+Iy2)
            #局部极大值点
            if (R>thsd):  #阈值的选择可以根据输入图片的长宽M、N等进行优化。
                
                if len(cornerArr)==0:
                    cornerArr.append([i,j])
                    pass
                [m,n]=cornerArr[-1]
                if ((j-n)<4 and (i-m<3)): #角点边缘几个像素重复满足情况的问题，目前解决得不太好
                    pass
                else:
                    #print(i,j,R)
                    cornerArr.append([i,j])
                
    
    markCorner(img,cornerArr)
    
            
def markCorner(img,cnarr):
    colImg=img.convert("RGB")#转换为彩色模式
    dPlant=ImageDraw.Draw(colImg)
    if cnarr==[]:
        print('thsd')
        return 
    print(len(cnarr))
    for cr in cnarr: #cr[0]->i cr[1]->j
        dPlant.ellipse((cr[1]-1,cr[0]-1,cr[1]+3,cr[0]+3),outline=190)
    
    colImg.show()
    colImg.save("./outputColorImg4.jpeg")



def dxFilter(imgArr,fx=''): 
    
    M=imgArr.shape[0]  #M对应x，N对应y
    N=imgArr.shape[1]
    lst=np.zeros((M,N),dtype=int)
    if fx=='':
        fx=[-2,-1,0,1,2]
    for i in range(0,M):
        for j in range(2,N-2):
            if j<2:  #0,1
                lst[i][j]=fx[2]*imgArr[i,j]+fx[3]*imgArr[i,j+1]+fx[4]*imgArr[i,j+2]
            #elif j>=N-3:
                #lst[i][j]=fx[0]*imgArr[i,j]+fx[1]*imgArr[i,j+1]+fx[2]*imgArr[i,j]
            else:
                lst[i][j]=fx[0]*imgArr[i,j-2]+fx[1]*imgArr[i,j-1]+fx[2]*imgArr[i,j]+fx[3]*imgArr[i,j+1]+fx[4]*imgArr[i,j+2]
    return lst
def dyFilter(imgArr,fy=''):
    return dxFilter(imgArr.transpose(),fy)

def mainHarris():
    img1=Image.open("./checkerboard.png")
    img2=Image.open("./stark512x512.jpg")
    img3=Image.open("./stark_coolone.jpg")
    img4=Image.open("./outputColorImg1.jpeg")
    img5=Image.open("./checkerboard.png")
    harrisPy(img2,5997979666)
    
    
def lowpic():
    img=Image.open("./checkerboard.png")
    #im=img.convert("L")
    #im.show()
    iarr=np.array(img)
    print(iarr.shape[0],iarr.shape[1]  )
    
if __name__ == '__main__':
    mainHarris()
    lowpic()
    
'''
输入图片，判断图片数组情况，只取一个灰度。
imgData-->np.array


486 
371790
12061708175.1
3537979666
9900568518.19
264265664-
参考资料：

[harris角点检测原理步骤说明](http://www.doc88.com/p-6721173911782.html)
[numpy.gradient.](https://docs.scipy.org/doc/numpy/reference/generated/numpy.gradient.html)
'''