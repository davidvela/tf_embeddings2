# progB
path = "./"
with open(path + 'newfile2.txt', 'w') as newfile:
    while True:
        # m = input('progB is running ')
        m = 'progB is running '
        print (m)
        newfile.write(m)
