def fibo(n):
  a = 0
  b = 1
  if n < 0:
    print("Invalid Input")
  elif n == 0:
    print(a)
  elif n == 1:
    print(b)
  else:
    print(a, b, end=" ")
    for i in range(2, n+1):
      c = a + b
      print(c, end=" ")
      a = b
      b = c
print("Fibonacci Series Program : ")
n = int(input("Enter the number of terms you want to print : "))
fibo(n)
print()
