# Find the counts of elements of an unsorted integer array which are equal to the average of all elements of that array.
# Ex:
# Input Case 1:  
# input: [2,2,2,2,2] 
# output:  5
# solution : 2+ 2+ 2+ 2+ 2 = 10/5 ==> 2
# it contain five 2 element

# Input Case 2:  
# input: [

# 1,3,2,4,5]  
# output:  1
# solution : 1+ 3+ 2+ 4+ 5 = 15/5 ==> 3
# it contain one 3 element
#SOlution:
a=int(input())
b=[]
for i in range(a):
    c=input()
    b.append(c)
summ=0 
avg=0
count=0
for i in b:
    summ=summ+int(i)
avg=summ//len(b)
for i in b:
    if(int(i)==avg):
        count+=1
print(count)