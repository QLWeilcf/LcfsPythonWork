#coding=utf-8


from  math import sqrt
import time
import turtle
turtle.screensize(900, 800)
sin=sqrt(3)/2  #sin(60°)
pc=50   #缩放因子，pc=50说明可以把1x1的格子通过50x50像素绘制出来

x,y=7,5

'''
sin=math.sqrt(3)/2
turtle.goto(x*pc,0)
turtle.goto(x*pc+pc*y*0.5,pc*sin*y)
turtle.goto(pc*y*0.5,pc*sin*y)
turtle.goto(0,0)
'''
t1= turtle.Turtle()  #绘制格子和分酒路径用
t2= turtle.Turtle()  #绘制文字

def drawDiamond(x,y,turtle=turtle,pc=pc,sin=sin):  #画边界
	turtle.pensize(3)
	drawToXY(x,0,turtle,sin)
	drawToXY(x,y,turtle,sin)
	drawToXY(0,y,turtle,sin)
	drawToXY(0,0,turtle,sin)#外框
	turtle.pensize(1)
	turtle.penup()
	drawText(-5,-15,'(0,0)',turtle,size=8)
	
	for j in range(1,y):  #画横线
		drawText(j*pc*0.5-20,pc*sin*j-4,'({0},{1})'.format(0,j),turtle,size=8)
		turtle.penup()
		drawToXY(0,j,turtle,sin)
		turtle.pendown()
		drawToXY(x,j,turtle,sin)
		drawToXY(x-y+j,y,turtle,sin)
		drawText(x*pc+pc*j*0.5+5,pc*sin*j-4,'({0},{1})'.format(x,j),turtle,size=8)
		turtle.penup()
	drawText(y*pc*0.5-20,pc*sin*y+5,'({0},{1})'.format(0,y),turtle,size=8)

	for i in range(1,x):  #画斜线 斜向右
		drawText(i*pc-5,-15,'({0},{1})'.format(i,0),turtle,size=8)
		turtle.penup()
		drawToXY(i,0,turtle,sin)
		turtle.pendown()
		drawToXY(i,y,turtle,sin)
		drawText(i*pc+pc*y*0.5-5,pc*sin*y+5,'({0},{1})'.format(i,y),turtle,size=8)
		turtle.penup()
	drawText(x*pc-5,-15,'({0},{1})'.format(x,0),turtle,size=8)
	drawText(x*pc+pc*y*0.5-5,pc*sin*y+5,'({0},{1})'.format(x,y),turtle,size=8)
	turtle.penup()
	for i in range(1,x+1):  #画斜线 斜向左
		drawToXY(i,0,turtle,sin)
		turtle.pendown()
		k=y if i>y else i   #min(i,y)
		w=i-y if i>y else 0
		drawToXY(w,k,turtle,sin)
		turtle.penup()
	turtle.goto(x*pc,0)  #开始画画的地方
	#turtle.goto(0*pc+0.5*y*pc,pc*sin*y)  #开始画画的地方
	turtle.pendown()

def drawToXY(x,y,turtle=turtle,sin=sin):
	turtle.goto(x*pc+0.5*y*pc,pc*sin*y)
	
def drawText(x,y,txt,turtle=turtle,size=14):
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()
	turtle.write(txt, font=("微软雅黑", size, "normal"))
	
def drawPlst(plst,turtle=turtle,t2=t2): #依照路径绘制出来
	dt=25
	dy=200
	k=0
	for p in plst:
		drawText(-180,dy-k*dt,str(p),t2,size=14)
		drawToXY(p[0],p[1],t1)
		k+=1

def zeroPath(x,y,turtle=turtle,pc=pc,sin=sin):
	turtle.pensize(3)
	drawToXY(5,0,turtle,sin)
	drawToXY(5,3,turtle,sin)
	drawToXY(0,3,turtle,sin)
	drawToXY(0,0,turtle,sin)#外框
	turtle.pensize(1)
	turtle.color("red")
	turtle.penup()
	turtle.goto(0,-2)
	turtle.pendown()
	turtle.color("red","red")
	turtle.begin_fill()
	turtle.circle(4)
	turtle.end_fill()
	turtle.penup()
	turtle.goto(x*pc+0.5*y*pc,pc*sin*y-2)
	turtle.pendown()
	turtle.begin_fill()
	turtle.circle(4)
	turtle.end_fill()
	turtle.color("black")
	turtle.pensize(1)
	turtle.penup()
	drawText(-5,-15,'(0,0)',turtle,size=8)
	
	for j in range(1,y):  #画横线
		turtle.penup()
		drawToXY(0,j,turtle,sin)
		turtle.pendown()
		drawToXY(x,j,turtle,sin)
		drawToXY(x-y+j,y,turtle,sin)
		turtle.penup()
		

	for i in range(1,x):  #画斜线 斜向右
		turtle.penup()
		drawToXY(i,0,turtle,sin)
		turtle.pendown()
		drawToXY(i,y,turtle,sin)
		turtle.penup()
		
	drawText(x*pc+pc*y*0.5-5,pc*sin*y+5,'({0},{1})'.format(x,y),turtle,size=8)
	turtle.penup()
	for i in range(1,x+1):  #画斜线 斜向左
		drawToXY(i,0,turtle,sin)
		turtle.pendown()
		k=y if i>y else i   #min(i,y)
		w=i-y if i>y else 0
		drawToXY(w,k,turtle,sin)
		turtle.penup()
	turtle.goto(x*pc,0)  #开始画画的地方
	#turtle.goto(0*pc+0.5*y*pc,pc*sin*y)  #开始画画的地方
	turtle.penup()


def onePath(x,y,turtle=turtle,pc=pc,sin=sin):
	turtle.pensize(3)
	drawToXY(5,0,turtle,sin)
	drawToXY(5,3,turtle,sin)
	drawToXY(0,3,turtle,sin)
	drawToXY(0,0,turtle,sin)#外框
	
	turtle.pensize(1)
	drawText(pc*y*0.5-5,pc*sin*y+5,'({0},{1})'.format(0,y),turtle,size=8)
	drawText(x*pc-5,-15,'({0},{1})'.format(x,0),turtle,size=8)
	turtle.penup()
	drawToXY(y,0,turtle,sin)
	turtle.pendown()
	drawToXY(0,y,turtle,sin)
	turtle.penup()
	turtle.goto(x*pc,0)  #开始画画的地方
	turtle.pendown()
	drawToXY(x-y,y,turtle,sin)
	turtle.penup()
	
	turtle.color("red")
	turtle.penup()
	turtle.goto(pc*y*0.5,pc*sin*y-2)
	turtle.pendown()
	turtle.color("red","red")
	turtle.begin_fill()
	turtle.circle(4)
	turtle.end_fill()
	turtle.penup()
	turtle.goto(x*pc,-2)
	turtle.pendown()
	turtle.begin_fill()
	turtle.circle(4)
	turtle.end_fill()
	turtle.color("black")
	turtle.pensize(1)
	turtle.penup()

# 生成倒酒状态转移路径
t=8
e=4
x,y=5,3
if y>x:
    x,y=y,x #保证x>y
r={}  #边界点对应的路径树
r[(0,0)]=[]
r[(x,y)]=[]
r[(x,0)]=[(x-y,y)]
r[(0,y)]=[(y,0)]
for n in range(1,x):
    if n<y:
        r[(n,0)]=[(0,n),(n,y)]
    else:
        r[(n,0)]=[(n-y,y),(n,y)]
    k=n+y
    if k>x:
        r[(n,y)]=[(n,0),(x,n+y-x)]
    else:
        r[(n,y)]=[(n,0),(n+y,0)]
for m in range(1,y):
    #m必然要小于x if m<x:  不需要
    r[(0,m)]=[(m,0),(x,m)]
    r[(x,m)]=[(0,m),(x+m-y,y)]

w=[x,0]  #上一个点
s=[x,0]
plst=[s] #开始
while s[0]!=e and s[1]!=e:
    ss=(s[0],s[1])
    sw=r[ss]
    slen=len(sw)
    
    if slen==1:
        w=s.copy()
        s[0]=sw[0][0]
        s[1]=sw[0][1]
    elif slen==2:
        if sw[0][0]==w[0] and sw[0][1]==w[1]:
            w=s.copy()
            s[0]=sw[1][0]
            s[1]=sw[1][1]
        elif sw[1][0]==w[0] and sw[1][1]==w[1]:
            w=s.copy()
            s[0]=sw[0][0]
            s[1]=sw[0][1]
        else:
            print(s,sw,slen)
    else:
        print(s,sw,slen)
    plst.append(s)

	
drawDiamond(x,y,t1)




#turtle.penup()

#time.sleep(7)
#plst=[(5,0),(2,3),(2,0),(0,2),(5,2),(4,3)]	
#plst=[(0,3),(3,0),(3,3),(5,1),(0,1),(1,0),(1,3),(4,0)]	
#plst=[(7,0),(2,5),(2,0),(0,2),(7,2),(4,5),(4,0),(0,4),(7,4),(6,5)]	
t1.color("red")
#t1.speed(1)
drawPlst(plst,t1,t2)


time.sleep(50)



