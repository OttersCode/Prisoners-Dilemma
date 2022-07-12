#Prisoners Dilema.py

import random

prisoners = 100
boxes = []
total = 0
testsize = 10000

for i in range (0,prisoners):
    boxes.append(i)

print("Initialisation complete")
#print(boxes)
for i in range(1,testsize):
    successes = 0
    random.shuffle(boxes)
    for prisoner in range(0,prisoners):
        check = 0
        nextbox = prisoner
        breakout = 0
        while ( check < prisoners/2) and (breakout != 1) :
            if boxes[nextbox] == prisoner:
                successes += 1
                
                breakout = 1
            nextbox = boxes[nextbox]
            check += 1
    #print(successes)
    if successes == prisoners:
        total += 1
        #print(total)

print(total/testsize)