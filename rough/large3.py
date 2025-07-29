a=int(input())
b=int(input())
c=int(input())
print(a,b,c,sep="-")
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)
