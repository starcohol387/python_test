n=eval(input())
for i in range(n):  #印第幾列，n列
    for j in range(1,i+2):  #印幾個星，從1開始印到i+2顆星 wtf
        print(i+j,end=' ')

    print('')
