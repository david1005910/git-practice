print("Fibonacci number")

n = 10

fibo = [0]*(n)
fibo[0] = 0
fibo[1] = 1

for i in range(2,n):
  fibo[i] = fibo[i-1] + fibo[i-2]

print(fibo)

