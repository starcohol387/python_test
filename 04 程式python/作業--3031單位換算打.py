x=input()
if(eval(x)%12==0):
    print(eval(x)//12, 'dozen')
else:
    print(eval(x)//12, 'dozen and', eval(x)%12)
