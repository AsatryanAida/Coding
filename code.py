n=int(input())
a=[]
list(a)
for i in range(n):
    m=list(input())
    a=a.append(m)

a=map(int(a))
print(sum(a))