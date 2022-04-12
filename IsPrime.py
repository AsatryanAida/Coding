n= int(input())
def isPrime(n):
    for i in range(2, n):
        d=2
        while i%d!=0:
            d+=1
        if d==i:
            print(i) 

print(isPrime(n))