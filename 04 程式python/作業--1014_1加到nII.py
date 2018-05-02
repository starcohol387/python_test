#這題我不會QQ

x=eval(input())
sum1=0
for i in range(1,x+1):  #x的值從1到x
    sum1+=i
    print(i,end='')     #我沒寫qq，就是把換行弄不見，然後把中間過程列出來
    if(i<x):            #如果迴圈不是最後一次執行時，要印'+'號
        print('+',end='')
else:
    print(' =',sum1)     
