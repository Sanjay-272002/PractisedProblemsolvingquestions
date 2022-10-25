count=0
r=[]

def beauty(c):
    global r
    global count
    if c in r:
        return 
    else:
        r.append(c)
        c=c+1
        c=str(c)
        c=c.rstrip('0')
        c=int(c)
        count=count+1
        beauty(c)
a=int(input());  
b=beauty(a)
print(count)   