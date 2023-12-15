#Question 6-2:
def ack(m,n):
    if m==0:
        return n+1
    elif m>0 and n==0:
        return ack(m-1,1)
    elif m>0 and n>0:
        return ack(m-1,ack(m,n-1))
        
#print(ack(3,4)

#Question 6-3:
def is_palindrome(st):
    return st==st[::-1]
# print(is_palindrome("rotator"))
# Question 6-4:
def is_power(a,b):
    if a/b:
        v=b**a
        return v, True 
    else:
        return False
#print(is_power(4,2))

# Question 6-5:
def gcd(a,b):
    if a<b:
        a, b = b%a, a % b 
        return a
    elif b<a:
         a, b = a%b, b%a
         return b

print(gcd(20,48))
        

