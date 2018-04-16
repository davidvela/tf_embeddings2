# progA
path = "./"
with open(path + 'newfile1.txt', 'w') as newfile:
    while True:
        m = 'progA is running '
        print (m)
        newfile.write(m)
