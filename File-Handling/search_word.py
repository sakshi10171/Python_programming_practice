# Search word in file

word = input("Enter word to search: ")
found = False

with open("file.txt", "r") as f:
    for line in f:
        if word in line:
            found = True
            break

if found:
    print("Word found in file")
else:
    print("Word not found")
