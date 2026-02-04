#Python program to check number is prime or not

num = int (input("Enter the number"))

if(num <= 1):
  print("Number is not a prime number")

else:
  is_prime = True
  for i in range(2, num // 2 + 1):
    if num % i == 0:
      is_prime = False
      break

  if is_prime:
    print("Prime number")
  else:
    print("Not a prime number")
