#python program to find second largest element in list

n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
  lst.append(int(input()))

lst = list(set(lst))
lst.sort()

print("Second largest element: " , lst[-2])
