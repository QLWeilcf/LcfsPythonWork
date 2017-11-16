# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 19:58:36 2017
按照卷积核的高通滤波似乎还有些问题，增强的边界灰度值接近于0；对于直接卷积核得到的超出255的值是直接用uint8转回灰度的，不知道有没有更好的方法。
@author: Ricardolcf


"""
import tensorflow as tf
from PIL import Image
import numpy as np

img1=Image.open("D:/python_works/lcf201610plus/RSimgPress2017/stark_coolone.jpg")
img2=Image.open("D:/python_works/lcf201610plus/RSimgPress2017/stark32x32.bmp")
img3=Image.open("D:/python_works/lcf201610plus/RSimgPress2017/fft2d_inpy/spydyhomecoming512x512.bmp")
img4=Image.open("D:/python_works/lcf201610plus/RSimgPress2017/fft2d_inpy/spydylowpass2.bmp")
iarr=np.array(img3)
iaa16=np.float16(iarr)
xw=iarr.shape[0]
yh=iarr.shape[1]
print(xw,yh)
#iaepd=np.expand_dims(iarr,0)
#iaary=np.float16(iaepd)

#Input: x
x_image = tf.placeholder(tf.float16,shape=[xw,yh])
x = tf.reshape(x_image,[1,xw,yh,1])

#Filter: W
hpfil = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]],dtype=np.float16)
hpf2=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]],dtype=np.float16)
hp3=np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]],dtype=np.float16)
hp4=np.array([[1,-2,1],[-2,5,-2],[1,-2,1]],dtype=np.float16)

lp1=np.array([[0.111,0.111,0.111],[0.111,0.111,0.111],[0.111,0.111,0.111]],dtype=np.float16)
lp2=np.array([[0.1,0.1,0.1],[0.1,0.2,0.1],[0.1,0.1,0.1]],dtype=np.float16)
#lp3=np.array([[0.111,0.111,0.111],[0.111,0.111,0.111],[0.111,0.111,0.111]],dtype=np.float16)




#W = tf.Variable(lp2)
W = tf.Variable(hp4)
W = tf.reshape(W, [3,3,1,1])
k=tf.Variable(np.array([[1]],dtype=np.float16))
k= tf.reshape(k, [1,1,1,1])
#print(W)
#print(np.float16(W))
#Stride & Padding
strides=[1, 1,1, 1]
padding='SAME'

#Convolution
y = tf.nn.conv2d(x, W, strides, padding)

init = tf.initialize_all_variables()


#x_data = np.array([[1,0,0,0,0],[2,1,1,2,1],[1,1,2,2,0],[2,2,1,0,0],[2,1,2,1,1]],dtype=np.float32)

with tf.Session() as sess:
    
    sess.run(init)

    #x = (sess.run(x, feed_dict={x_image: iaa16}))
    #W = (sess.run(W, feed_dict={x_image: iaa16}))
    y = (sess.run(y, feed_dict={x_image: iaa16}))

    #print(iaa16)
    print ("The shape of y:\t", y.shape)
    #print (y.reshape(xw,yh))
    print(y)
    
    yaq=y.reshape(xw,yh)
    #op1=np.array(yaq)/9
    yaqw=np.uint8(yaq)
    print(yaqw)
    im_t = Image.fromarray(yaqw)
    #im_t.save('D:/python_works/lcf201610plus/RSimgPress2017/fft2d_inpy/spydylowpass3.bmp')
    im_t.show()
    






'''
inputImg = tf.Variable([1,x,y,3],dtype='float16')
inputma = tf.Variable(iaepd,dtype='float16')

filT = tf.Variable([x,y,3,3],dtype='float16')
opone = tf.nn.conv2d(iaary, filT, strides=[1, 2, 2, 1], padding='SAME')
biases = tf.get_variable('biases',[1],initializer = tf.constant_initializer(1))
bias = tf.nn.bias_add(opone, biases)

init = tf.initialize_all_variables()

with tf.Session() as sess:
    sess.run(init)
    sess.run(opone)
    conv_M = sess.run(bias,feed_dict={x:iaary})
    print(type(conv_M))
    im_t = Image.fromarray(conv_M)
    im_t.show()
'''
'''

参考：
[滤波和卷积](http://www.cnblogs.com/wangyu2013/articles/2846013.html)
[如何实现空洞卷积](http://blog.csdn.net/mao_xiao_feng/article/details/78003730)

'''
