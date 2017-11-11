import random


def coin_tosses(numberOfTosses):
    numberOfHeads = 0
    numberOfTails = 0
    for i in range(1, numberOfTosses + 1):
        x = random.random()
        x_rounded = round(x)
        if x_rounded == 0:
            numberOfHeads += 1
            print "Attempt #" + str(i) + ": Throwing a coin... It's a head! ... Got " + str(numberOfHeads) + " head(s) so far and " + \
                  str(numberOfTails) + " tail(s) so far"
        else:
            numberOfTails += 1
            print "Attempt #" + str(i) + ": Throwing a coin... It's a tail! ... Got " + str(numberOfHeads) + " head(s) so far and " + \
                  str(numberOfTails) + " tail(s) so far"


coin_tosses(5000)
