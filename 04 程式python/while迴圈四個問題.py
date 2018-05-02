#不會：要輸出總合、平均、最大值、位置
sum=n=0
count=-1
maxval=0       #讓python默念最大數
maxpos=0


while n!=-1:
    count+=1
    sum+=n
    #如果本次輸入>目前已知最大值，就將本次輸入設定為目前最大值，順便讓python記位置
    if n>maxval:
        maxval=n #注意賦予左右
        maxpos=count
        
    n=eval(input())
else:
    print(sum)
    print(sum/count)
    print(maxval)#最大值
    print(maxpos)
    
