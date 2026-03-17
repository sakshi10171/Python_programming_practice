#python program to check number is armstrong or not

num = int(input("Enter the number: "))
original = num
sum = 0

while num != 0:
  digit = num % 10
  sum += digit ** 3
  num //= 10

if sum == original:
  print("Armstrong number")
else:
  print("Not an armstrong number")
