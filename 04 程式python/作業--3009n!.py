x=eval(input())
n1=1                 #將n給定初始值
for i in range(x,1,-1): #讓x從x迭代到1
    n1*=i
else:
    print(n1)
