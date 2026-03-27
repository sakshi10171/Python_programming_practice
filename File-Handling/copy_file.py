# Copy content from one file to another

with open("file.txt", "r") as source:
    content = source.read()

with open("copy.txt", "w") as target:
    target.write(content)

print("File copied successfully")
