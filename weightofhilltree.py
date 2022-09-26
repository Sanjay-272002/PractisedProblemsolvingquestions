level=input()
firstr=int(input())
incremnet=int(input())
a=[]
summ=1
addd=0
sa=0
s=0
for i in range(int(level)):
    a.append(summ)
    summ=summ+2
for i in a:
    for j in range(1,i+1):
        if(j%2)!=0:
            sa=firstr
            addd=addd+sa 
        else:
            addd+=s
    s=firstr
    firstr+=2
print(addd)