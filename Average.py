# Find the average of largest and smallest numbers in an unsorted integer array?
# Eg. 
# Input Case 1:  
# input: [1, 4, 3, 2]
# output:  2.5
# solution : average = (1+4)/2 =>5/2 => 2.5

# input: [1, 4, 3, 4]
# output:  3
# solution : average = (1+4 +4)/3 =>9/3 => 3

#Solution
a=int(input())
b=[]
for i in range(a):
    c=input()
    b.append(c)
maxx=b[0]
minn=b[0]
c=[]
summ=0
# for maximum
for i in range(len(b)):
    if(b[i]>maxx):
        maxx=b[i]
#for minimum
for i in range(len(b)):
    if(b[i]<minn):
        minn=b[i]
for i in b:
    if(int(i)==int(maxx)):
        c.append(i)
    elif(int(i)==int(minn)):
        c.append(i)
        
    else:
        continue
for i in c:
    summ=summ+int(i)
    
print(summ/len(c))