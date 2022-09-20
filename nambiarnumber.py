def nambiarnumber(number,i):
    if i>len(number):
        return ""
        
    firstnumber=ord(number[i])-ord('0')
    summ=0
    result = ''
    while i<len(number):
        firstNumberRem = firstnumber%2
        summ=summ+(ord(number[i])-ord('0'))
        summRem = summ % 2
        if firstNumberRem == summRem:
            if(i==len(number)-1):
                result +=str(summ)
            i=i+1
        else:
            result += str(summ)
            summ = 0
            i=i+1
            firstnumber = number[i]
            firstnumber=ord(number[i])-ord('0')
    return result        
    
number='9880127431'
i=0
print(nambiarnumber(number,i))