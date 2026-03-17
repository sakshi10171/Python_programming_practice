#python program to find largest element in a list

n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
  lst.append(int(input()))

largest = lst[0]

for num in lst:
  if num > largest:
    largest = num

print("Largest element: ", largest)
