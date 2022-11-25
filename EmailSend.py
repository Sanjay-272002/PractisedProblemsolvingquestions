#Given n email addresses of different domains, please send an email to the first address(in alphabetical order) of each domain. Please assume a function sendmail() to send the emails.
# (note: give general solution).
# Input Array = ['ghi@hotmail.com', 'def@yahoo.com', 'ghi@gmail.com', 'abc@channelier.com', 'abc@hotmail.com', 'def@hotmail.com', 'abc@gmail.com', 'abc@yahoo.com', 'def@channelier.com','jkl@hotmail.com', 'ghi@yahoo.com', 'def@gmail.com'].

# Expected Output - Below is the  order of address in which sendmail function is going to send mail.
#                                 abc@channelier.com
#                                 abc@yahoo.com
#                                 abc@gmail.com
#                                 abc@hotmail.com
#Solution:

def sendmail(b):
    d=[]
    e=[]
    f=[]
    #to append first letter of each word
    for i in b:
        d.append(i[0])
    #to change string to unicode
    for i in d:
        e.append(ord(i)-ord('0'))
    print(e)
    m=e[0]
    #comparing Unicode numbers
    for i in range(len(e)):
        if(e[i]<m):
            m=e[i]
    m=m+ord('0')
    m=chr(m)
    #appending the words in list in alphabetical order
    for i in b:
        if(i[0][0]==m):
            f.append(i)
    for i in f:
        print(i)
        
        

a=int(input())
b=[]
for i in range(a):
    c=input()
    b.append(c)

c=sendmail(b)