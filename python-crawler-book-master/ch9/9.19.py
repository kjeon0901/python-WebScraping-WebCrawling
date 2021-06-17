file = open('ch.9.n.txt', 'a')

for i in range(0, 5):
    file.write(str(i) + '\n')

file.close()
