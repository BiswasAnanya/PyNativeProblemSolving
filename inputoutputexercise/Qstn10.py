# Read line number 4 from the following file

with open ("Firstfile.txt", "r") as fp:
    lines = fp.readlines()
    print(lines[3])