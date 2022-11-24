'''

                            Online Python Debugger.
                Code, Run and Debug Python program online.
Write your code in this editor and press "Debug" button to debug program.

'''

a=int(input())
b=[]
e=[]
f=0
for i in range (a):
    c=input()
    b.append(c)
for i in range(a-1):    
    if((b[i]>b[i+1]) or (b[len(b)-1]==1)):
        c=i
        break
    for i in range(c,a-1):
       if((b[i]>b[i+1]) or (b[len(b)-1]==1)): 
        e.append(b[i])
       elif(b[i]==b[i+1]):
           e.append(b[i])
           f=i+1
           break
       else:
           f=i
           break
        
    if(f>0):
        for i in range(f,a-1):
            if((b[i]<b[i+1]) or (b[len(b)-1]==1) ): 
                e.append(b[i])
            else:
                g=i
                break
    if(g<len(b-2)):
        for i in range(g,a-1):
            if((b[i]>b[i+1]) or (b[len(b)-1]==1)): 
                e.append(b[i])



z=len(b)
y=len(e)
if(f==0):
    print('0')
elif(b[z-1]>e[y-1]):
    e.append(b[len(b-1)])
    print(len(e))
else:
    print(len(e))
