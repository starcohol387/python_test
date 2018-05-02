x=int(input())
y=int(input())
z=int(input())

if(x+y<=z): #沒有排序xyz大小，所以要都考慮
    print('False')
elif(x+z<=y):
    print('False')
elif(z+y<=x):
    print('False')
else:
    print('True')
    if(x*x+y*y==z*z): #不能打x^2而要打x*x
        print('Right Triangle')
    elif(x*x+z*z==y*y):
        print('Right Triangle')
    elif(z*z+y*y==x*x):
        print('Right Triangle')
    else:
        print('Non-Right Triangle')
        

