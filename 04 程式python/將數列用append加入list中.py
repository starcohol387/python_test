#將數列以append加入list當中，-1結束，list中沒有-1

x=[]                 #令一個list
while True:          #不知道次數的迴圈用while
    n=eval(input())
    if n==-1:        #這樣的寫法可以達到-1結束且-1不會進入list
        break
    x.append(n)
print(x)

#將list中數，由小到大排序>>>在shell中x.sort()
#在第四個位置插入一整數10>>>在shell中x.insert(位置,物件)>>>x.insert(3,10)
                                                       #0,1,2,3
#印出list中有幾個整數10>>>shell中x.count(10)
#將其由大到小排序>>>這時不能用x.reverse>>>10還是會在倒數第四位喔
 #得先正常排序再reverse
