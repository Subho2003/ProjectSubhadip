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
    for i in range(2, n):
      c = a + b
      print(c)
      a = b
      b = c
print("Fibonacci Series Program : ")
n = int(input("Enter the number of terms you want to print : "))
fibo(n)
