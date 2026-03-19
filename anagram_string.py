#python program to check whether two strings are anagram

str1 = input("Enter first string : ")
str2 = input("Enter second string: ")

str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

if sorted(str1) == sorted(str2):
  print("Strings are anagram")
else:
  print("Strings are not anagram")
