#coding=UTF-8
'''readme:
利用结巴库对文本（一些txt格式的书）进行词频统计等；
更深入的分析可以写为其他函数；
结合词云图库进行可视化，输出支持csv，txt格式（先不考虑xls格式）
要求：能快速对任何一本小说（txt版）运行，快速得出结果；
再加上停用词表

'''

from collections import Counter
import jieba


def wordFriZero(filePath,savePath):
    #该函数将词频统计结果输出为一个txt文件。filePath是输入文件的完整路径；savePath是输出文件的路径
    import re
    words=[]
    with open(filePath,'rb') as f: #出现编码错误时把 r 改为 rb
        all_w=f.readlines()
        for w in all_w:
            if w!='':
                sk=list(jieba.cut(w))
                patzer = re.compile(r'[\u4e00-\u9fa5]+')
                for i in sk:
                    pu=patzer.search(i)
                    if pu != None:
                        d=pu.group()
                        words.append(d)#这里千万不能用extend，这和extend的机制有关吧，如果extend传入的参数不是列表，
                        #例如是字符串，则会拆分掉。在这里我debug了好久。
    count=Counter(words)
    result = sorted(count.items(), key=lambda x: x[1], reverse=True)
    with open(savePath,'a+') as fi:
        for wd in result:
            fi.write(str(wd)+'\n')
    print('wordFriZero finish')

def countFriInf(fpath):#fpath 为一个每行一个单词/数字的文件
    #统计重复次数,file->list->dict
    #50\n 3\n 4\n 3\n->  ['50','2','4']  ->{'50':1,'3':2,'4':1}
    savePath="D:/python_works/OthersExcellentProject/crossin-learn-python-master/Ric2017to1108wsa.txt"
    with open(fpath,'r') as f:
        all_ws=f.readlines()
    count=Counter(all_ws)
    result = sorted(count.items(), key=lambda x: x[1], reverse=True)
    with open(savePath,'a+') as fi:
        for wd in result:
            fi.write(str(wd[1])+","+wd[0])
    print('countFriInf finish')

def cutWordInFile(filePath):
    #该函数将词频统计结果输出为一个txt文件。filePath是输入文件的完整路径；savePath是输出文件的路径
    import re
    words=[]
    with open(filePath,'rb') as f: #出现编码错误时把 r 改为 rb
        all_w=f.readlines()
        for line in all_w:
            if line!='':
                sk=jieba.lcut(line)#每一段切成list
                patzer = re.compile(r'[\u4e00-\u9fa5]+')
                for i in sk:
                    pu=patzer.search(i)
                    if pu != None:
                        d=pu.group()
                        words.append(d)#这里千万不能用extend，这和extend的机制有关吧，如果extend传入的参数不是列表，
                        #例如是字符串，则会拆分掉。在这里我debug了好久。
    count=Counter(words)
    result = sorted(count.items(), key=lambda x: x[1], reverse=True)
    print('cut finish')
    return result

def readStopWords(swfile):#swfile的组织？
    swlst=[]#读入停用词
    with open(swfile,'r',encoding='utf-8') as swf:
        all_line=swf.readlines()
        for el in all_line:
            swlst.append(el[:-1])
    
    return swlst

def saveResult(resl,savePath,mode='txt',stw=None):
    wmax=48
    if (mode=='csv' and stw==None):#最常用的输出
        with open(savePath,'a+') as ftxt:
            for wd in resl:
                if (wd[1]<wmax):
                    break
                ftxt.write(wd[0]+","+str(wd[1])+'\n')
    elif (mode=='csv' and stw!=None): #也是常用
        with open(savePath,'a+') as ftxt:
            for wd in resl:
                if (wd[1]<wmax):
                    break
                elif (wd[0] in stw):
                    continue
                else:
                    ftxt.write(wd[0]+","+str(wd[1])+'\n')
    elif (mode=='txt' and stw!=None):
        with open(savePath,'a+') as ftxt:
            for wd in resl:
                if (wd[1]<wmax):
                    break
                if (wd[0] in stw):
                    continue
                else:
                    ftxt.write(wd[0]+" : "+str(wd[1])+'\n')    
    elif (mode=='online'and stw!=None):
        with open(savePath,'a+',encoding='utf-8') as ftxt:
            for wd in resl:
                if (wd[1]<wmax):
                    break
                if (wd[0] in stw):
                    continue
                else:
                    ftxt.write(wd[0]+'\n')
    elif (mode=='wc' and stw!=None):
        all_dist={}
        for wd in resl:
            if (wd[1]<wmax):
                break
            if (wd[0] in stw):
                continue
            else:
                all_dist[wd[0]]=wd[1]
        toWordCl(all_dist)
    elif (mode=='wc' and stw==None):
        all_dist={}
        for wd in resl:
            if (wd[1]<wmax):
                break
            else:
                all_dist[wd[0]]=wd[1]
        toWordCl(all_dist)
    else:#txt stw==None
        with open(savePath,'a+') as ftxt:
            for wd in resl:
                ftxt.write(wd[0]+" : "+str(wd[1])+'\n')

def toWordCl(adist): #input ?
    from wordcloud import WordCloud
    wordcl = WordCloud(background_color = 'white',font_path='C:\Windows\Fonts\simsun.ttc')
    wordcloud=wordcl.generate_from_frequencies(adist)
    wordcloud.to_file('D:/python_works/OthersExcellentProject/crossin-learn-python-master/Rica2017to1108bawcloud2.png')

def anlyDailyData():
    import time
    na=time.time()
    filename='D:/python_works/OthersExcellentProject/crossin-learn-python-master/RicardolcfFrom2017to1108backup.txt'
    savefile = 'D:/python_works/OthersExcellentProject/crossin-learn-python-master/dailybaiyexingAnlyo3.txt'
    stopws = 'D:/python_works/OthersExcellentProject/crossin-learn-python-master/zhaolei/textStopWords.txt'
    resul=cutWordInFile(filename) #resul直接就是一个dict了吗？
    stwd=readStopWords(stopws)
    #saveResult(resul,savefile,'wc',stwd)
    saveResult(resul,savefile,'txt')
    print('Using time:',time.time()-na)
	
	
if __name__ == '__main__':
    fp="D:/python_works/OthersExcellentProject/crossin-learn-python-master/dailycsv11.csv"
    countFriInf(fp)




'''
D:/python_works/OthersExcellentProject/crossin-learn-python-master/zhaolei/textStopWords.txt
D:\文档618\Books\【书籍精选】\要看的\东野圭吾74本合集/白夜行.txt

'''
