#Python program to calculte factorial of number

num = int(input("Enter the number: "))

fact = 1

for i in range(1, num + 1):
  fact *= 1

print("Factorial of number: ",fact)
