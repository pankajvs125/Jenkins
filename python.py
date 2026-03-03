def sumof(n,sum=0,i=1):
    if i>n:
        return sum
    sum+=i
    return sumof(n,sum,i+1)
print(sumof(10))
