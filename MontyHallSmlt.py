# -*- coding: utf-8 -*-

def MontyHallSmlt(): #Monty Hall Simulation
    #三门问题的模拟
    import random 
    sltNum=1000 #模拟次数
    change=0
    win=[0,0,0,0] #总，不换对，换对，换的次数
    #door=[0,0,0]
    for i in range(0,sltNum+1):
        dst=random.randint(0,2) #随机一个门放羊
        chioce=random.randint(0,2)
        change=random.randint(0,1)
        if change==1:
            win[3]+=1
            
        if chioce==dst:
            if dst==0:#开门只是仪式性的
                if change==0: #不改 d[0]
                    win[0]+=1
                    win[1]+=1 #no else
            elif dst==1:
                if change==0:
                    win[0]+=1
                    win[1]+=1
            else:#odoor=0
                if change==0:
                    win[0]+=1
                    win[1]+=1
        else:    
            if chioce==0:
                if dst==1:# odoor=2
                    if change==1:
                        win[0]+=1
                        win[2]+=1
                elif dst==2:#odoor=1
                    if change==1:
                        win[0]+=1
                        win[2]+=1
            elif change==1:
                if dst==0:
                    if change==1:
                        win[0]+=1
                        win[2]+=1
                elif dst==2:
                    if change==1:
                        win[0]+=1
                        win[2]+=1
                
            elif change==2:
                if dst==1:
                    if change==1:
                        win[0]+=1
                        win[2]+=1
                elif dst==0:
                    if change==1:
                        win[0]+=1
                        win[2]+=1
    
    print(win)
    
if __name__ == '__main__':
    MontyHallsmlt()   
