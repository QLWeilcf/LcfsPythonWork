# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 00:36:55 2018

@author: Ricardolcf
"""

def readAndRe():
    filePath="L:/RSshiyan/L7_using_Test.txt"
    with open(filePath) as inpf:
        alllines=inpf.readlines()
        for i in alllines:
            print(i)
            if (i!=""):
                j=i.split()
                print(j)

def readGeoTif():#建立两个tif图像间像元的联系，输出为一个表格
    from PIL import Image
    import numpy as np
    from datetime import datetime
    start=datetime.now()
    landPath="L:/RSshiyan/tempTran2/L_2015_class_MaxLh_32.tif"
    lu_im=Image.open(landPath)
    lu_arr=np.array(lu_im)
    
    lst_p="L:/RSshiyan/QimoArcGISoutput/L7_2015_B157_9_r_arcReclass4.tif"
    lst=Image.open(lst_p)
    lst_arr=np.array(lst)
    x,y=lu_arr.shape
    with open("L:/RSshiyan/L7_2015_range_res4_20st.txt",'a+') as f:
        for i in range(0,x,20):
            for j in range(0,y,20):
                
                f.write(str(lu_arr[i][j])+","+str(lst_arr[i][j])+"\n")
                
                #i_r=[100,500,1200,2600]#抽样输出看看
                #j_r=[300,800,2100,2800]
                #if (i in i_r and j in j_r):
                    #print(lst_arr[i][j])
    
    print(datetime.now()-start)

def numGeoTif():#统计不同类别地物对应像元温度值，得到平均值、标准差，最大/小值等，支持过滤掉异常值
    from PIL import Image
    import numpy as np
    from datetime import datetime
    start=datetime.now()
    landPath="L:/RSshiyan/tempTran2/L_2015_class_MaxLh_32.tif"
    lu_im=Image.open(landPath)
    lu_arr=np.array(lu_im)
    
    lst_p="L:/RSshiyan/L7_2015_B157_9_res.tif"
    lst=Image.open(lst_p)
    lst_arr=np.array(lst)
    x,y=lu_arr.shape
    privi=[[1,1976576,0],[2,875461,0],[3,243054,0],[4,933559,0],\
           [5,576269,0],[6,692961,0],\
           [7,1299946,0],[8,367270,0],[9,396521,0],[10,83055,0]]
    a1=np.zeros(privi[0][1])
    a2=np.zeros(privi[1][1])
    a3=np.zeros(privi[2][1])
    a4=np.zeros(privi[3][1])
    a5=np.zeros(privi[4][1])
    a6=np.zeros(privi[5][1])
    a7=np.zeros(privi[6][1])
    a8=np.zeros(privi[7][1])
    a9=np.zeros(privi[8][1])
    a10=np.zeros(privi[9][1])
    #不适合用多维数组，就只能构造类似于switch的语法了
    
   
    for i in range(x):
        for j in range(y):
            now_lu=lu_arr[i][j]
            '''
            lst_n=lst_arr[i][j]
            if (lst_arr[i][j]<6):#除掉异常点
                lst_n=6
            elif (lst_arr[i][j]>19):
                lst_n=19
            '''
            if (now_lu==1):
                a1[privi[0][2]]=lst_arr[i][j]
                privi[0][2]+=1
            elif (now_lu==2):
                a2[privi[1][2]]=lst_arr[i][j]
                privi[1][2]+=1
            elif (now_lu==3):
                a3[privi[2][2]]=lst_arr[i][j]
                privi[2][2]+=1
            elif (now_lu==4):
                a4[privi[3][2]]=lst_arr[i][j]
                privi[3][2]+=1
            elif (now_lu==5):
                a5[privi[4][2]]=lst_arr[i][j]
                privi[4][2]+=1
            elif (now_lu==6):
                a6[privi[5][2]]=lst_arr[i][j]
                privi[5][2]+=1
            elif (now_lu==7):
                a7[privi[6][2]]=lst_arr[i][j]
                privi[6][2]+=1
            elif (now_lu==8):
                a8[privi[7][2]]=lst_arr[i][j]
                privi[7][2]+=1
            elif (now_lu==9):
                a9[privi[8][2]]=lst_arr[i][j]
                privi[8][2]+=1
            elif (now_lu==10):
                a10[privi[9][2]]=lst_arr[i][j]
                privi[9][2]+=1
            else:
                print(now_lu,lst_arr[i][j],i,j)
    u_pv=[[1,0,0,0,0],[2,0,0,0,0],[3,0,0,0,0],[4,0,0,0,0],\
           [5,0,0,0,0],[6,0,0,0,0],\
           [7,0,0,0,0],[8,0,0,0,0],[9,0,0,0,0],[10,0,0,0,0]]        
    
    u_pv[0][1]=a1.min()
    u_pv[0][2]=a1.max()
    u_pv[0][3]=a1.mean()
    u_pv[0][4]=a1.std()
    
    u_pv[1][1]=a2.min()
    u_pv[1][2]=a2.max()
    u_pv[1][3]=a2.mean()
    u_pv[1][4]=a2.std()
    
    u_pv[2][1]=a3.min()
    u_pv[2][2]=a3.max()
    u_pv[2][3]=a3.mean()
    u_pv[2][4]=a3.std()
    
    u_pv[3][1]=a4.min()
    u_pv[3][2]=a4.max()
    u_pv[3][3]=a4.mean()
    u_pv[3][4]=a4.std()
    
    u_pv[4][1]=a5.min()
    u_pv[4][2]=a5.max()
    u_pv[4][3]=a5.mean()
    u_pv[4][4]=a5.std()
    
    u_pv[5][1]=a6.min()
    u_pv[5][2]=a6.max()
    u_pv[5][3]=a6.mean()
    u_pv[5][4]=a6.std()
    
    u_pv[6][1]=a7.min()
    u_pv[6][2]=a7.max()
    u_pv[6][3]=a7.mean()
    u_pv[6][4]=a7.std()
    
    u_pv[7][1]=a8.min()
    u_pv[7][2]=a8.max()
    u_pv[7][3]=a8.mean()
    u_pv[7][4]=a8.std()
    
    u_pv[8][1]=a9.min()
    u_pv[8][2]=a9.max()
    u_pv[8][3]=a9.mean()
    u_pv[8][4]=a9.std()
    
    u_pv[9][1]=a10.min()
    u_pv[9][2]=a10.max()
    u_pv[9][3]=a10.mean()
    u_pv[9][4]=a10.std()
    
    
    with open("L:/RSshiyan/L7_2015_range_res1_c5.txt",'a+') as f:
        for k in range(10):
            f.write(str(u_pv[k][0])+','+str(u_pv[k][1])+','+str(u_pv[k][2])+','+\
                    str(u_pv[k][3])+','+str(u_pv[k][4])+','+str(privi[k][1])+','+str(privi[k][2])+'\n')
    
    print(datetime.now()-start)

def sumImgProv():# input: int float
    from PIL import Image
    import numpy as np
    landPath="L:/RSshiyan/tempTran2/L_2015_class_MaxLh_32.tif"
    lu_im=Image.open(landPath)
    lu_arr=np.array(lu_im)
    print(lu_arr)
    
    return

#sumImgProv()
#numGeoTif()
readGeoTif()
#readAndRe()
