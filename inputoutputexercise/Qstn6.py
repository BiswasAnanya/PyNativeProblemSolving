# write all file content into new file by skiping line 5 from following file

f = open("Firstfile.txt", 'w')
f.write('Now the file has one content\n')
f.write('Now the file has one content\n')
f.write('Now the file has one content\n')
f.write('Now the file has one content\n')
f.write('Now the file has one content\n')
f.write('Another new line')
f.close()

# Firstfile = open('Firstfile.txt', 'r')
# Secondfile = open('Secondfile.txt', 'a')
with open('Firstfile.txt', 'r') as Firstfile, open('Secondfile.txt', 'a') as Secondfile:
    for line in Firstfile:
        Secondfile.write(line)
# Firstfile.close()
# Secondfile.close()
