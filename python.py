def SumOfNatural(n,sum=0,i=1):
  if i>n:
    return sum
  sum+=i
  return SumOfNatural(n,sum,i+1)
print(SumOfNatural(10))
