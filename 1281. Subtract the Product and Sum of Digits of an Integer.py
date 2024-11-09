n = 234
s,p = 0,1
while n>0:   
    s+= n%10
    p*= n%10
    n=n//10

print(p-s)