n=int(input("Enter the range of the fibonacci series: "))
fibonacci=[0,1]
for x in range(n):
  if(x>1):
    num=fibonacci[x-2]+fibonacci[x-1]            
    fibonacci.append(num)
for x in fibonacci:
    print(x)
