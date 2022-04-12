def solution(number):
    a=[]
    for i in range(1, number):
        if i%3==0 or i%5==0:
            a.append(i)
    return(sum(a))

print(solution(4))