a = 0
b = 1
def fibo(n):
  if n < 0:
    print("Invalid Input")
  elif n == 0:
    return a
  elif n == 1:
    return b
  else:
    for i in range(2, n):
      c = a + b
      a = b
      b = c
      return b

print("Fibonacci Series Program : ")
n = int(input("Enter the number of terms you want to print : "))
print(fibo(n))
