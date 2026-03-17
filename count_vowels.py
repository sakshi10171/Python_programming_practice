#python program to count vowels in a string

text = input("Enter the string: ")
vowels = "aeiouAEIOU"

count = 0

for ch in text:
  if ch in vowels:
    count +=1

print("Number of vowels: " , count)
