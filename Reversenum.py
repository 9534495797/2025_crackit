def reverse(num):
    revnum=0
    
    while num:
        rem =num%10
        revnum=revnum*10+rem
        num//=10
        return revnum
    
    
n=int(input())
print(reverse(n))
