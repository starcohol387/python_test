x=int(input())
if(x==1):
    y=int(input())
    if(y<0 or y>100):
        print('score error')
    elif(y>=60):
        print('pass')
    else:
        print('fail')        
elif(x==2):
    y=int(input())
    if(y<0 or y>100):
        print('score error')
    elif(y>=70):
        print('pass')
    else:
        print('fail')
else:
    print('roll error')

#不需要打輸入的中文
#不能打x=1，記得if elif else後面要加:
