# Count number of characters in file

with open("file.txt", "r") as f:
    content = f.read()

# Remove spaces and newlines if you want pure characters
char_count = len(content)

print("Total characters:", char_count)
