# Count words in file

with open("file.txt", "r") as f:
    words = f.read().split()

print("Total words:", len(words))
