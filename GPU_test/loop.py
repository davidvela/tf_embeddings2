
import time 
import sys 

print ("Script started.")
stored_exception=None
epochs = 100
disp   = epochs / 100

for i in range(epochs):
    try:
        # do something time-cosnuming
        time.sleep(1)
        if i % disp == 0: print(i)
        if stored_exception:
            print(" finished.")
            break
        

    except KeyboardInterrupt:
        stored_exception = sys.exc_info()

print("Bye")

# if stored_exception:
#     raise stored_exception[0], stored_exception[1], stored_exception[2]

sys.exit()