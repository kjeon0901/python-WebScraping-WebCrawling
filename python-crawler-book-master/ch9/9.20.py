file = open('ch.9.n.txt', 'r')

lines = file.readlines()

print(lines, type(lines))

for line in lines:
    print(line)

file.close()    
