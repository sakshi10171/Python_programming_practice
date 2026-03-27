# Count number of lines in file

with open("file.txt", "r") as f:
    lines = f.readlines()

print("Total lines:", len(lines))
