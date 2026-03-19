#python program to remove duplicates from list

n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
  lst.append(int(input()))

unique_list = []

for num in list:
  if num not in unique_list:
    unique_list.append(num)

print("List after removing duplicates: " , unique_list)
