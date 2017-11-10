#coding=UTF-8
'''
findFileInWindows
快速运行，快速找文件
还是挺慢的，在D盘下找个文件，用了101秒；
考虑加上文件后缀的过滤
还有处理文件夹名称和名称相同的情况。
'''
import os


def marchFlie(filstr,fname):
    #import re  #输入为两个字符串，eg：123.pdf, 123
    #patzero=re.compile(r"")
    if (len(filstr)<len(fname)):
        return False
    elif (-1 !=filstr.find(fname)):
        return True
    else:
        return False

def fastInDisk(sttp,fname):
    #pa=[]
    for root,dirs,fileslst in os.walk(sttp):
        for filstr in fileslst:
            if marchFlie(filstr,fname):
                print(root,filstr,fname)
    #startPath="D:/"

def fastDiskWithRe(sttp,fileName):
    pass
    

if __name__ == '__main__':
    import time
    na=time.time()
    starPath="D:/教学课件及学习资料/程序设计/Others"
    fileN="易语言"
    fastInDisk(starPath,fileN)
    print('Using time:',time.time()-na)    







'''
改造成：能满足不同需求的找文件；如模糊查找、单文件查找
一旦找到文件停止执行；定制后缀名查找；配置常用查找目录，优先查找目录里面的内容
将文件去重功能整合进来。
'''






