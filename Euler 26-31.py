#number of unique powers with base and exponent ranging from 2-100
def prob29():
    setpowers = set()
    for a in range(2, 101):
        for b in range(2, 101):
            setpowers.add(pow(a, b))
    return len(setpowers)

#Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
def prob30():
    totalsum = 0
    uniquenums = set()

    maxperdigit = pow(9, 5)
    powerdict = {}
    for i in range(0, 10):
        powerdict[i] = pow(i, 5)

    maxNumDigits = 1
    smallestNum = 1
    while(True):
        if(maxperdigit*maxNumDigits < smallestNum):
            maxNumDigits -= 1
            break
        smallestNum *= 10
        maxNumDigits+=1

    bignumdict = {}
    smallnumdict ={}
    for i in range(0,10):
        bignumdict[i] = 0
        smallnumdict[i] = 0

    for k1,v1 in powerdict.iteritems():
        smallnumdict[k1] += 1
        for k2,v2 in powerdict.iteritems():
            smallnumdict[k2] += 1
            for k3,v3 in powerdict.iteritems():
                smallnumdict[k3] += 1
                for k4,v4 in powerdict.iteritems():
                    smallnumdict[k4] += 1
                    for k5,v5 in powerdict.iteritems():
                        smallnumdict[k5] += 1
                        for k6,v6 in powerdict.iteritems():
                            smallnumdict[k6] += 1

                            cursum = v1+v2+v3+v4+v5+v6
                            for curDigit in range(0, len(str(cursum))):
                                bignumdict[int(str(cursum)[curDigit])] += 1

                            for k in range(len(str(cursum)),6):
                                bignumdict[0] += 1

                            numsEqual = True;
                            for i in range(0,10):
                                if not smallnumdict[i] == bignumdict[i]:
                                    numsEqual = False
                                    break;

                            if (numsEqual == True) and (not cursum in uniquenums):
                                print cursum
                                totalsum += cursum
                                uniquenums.add(cursum)

                            #reset
                            for i in range(0,10):
                                bignumdict[i] = 0

                            smallnumdict[k6] -= 1
                        smallnumdict[k5] -= 1
                    smallnumdict[k4] -= 1
                smallnumdict[k3] -= 1
            smallnumdict[k2] -= 1
        smallnumdict[k1] -= 1

    return totalsum-1


#number of ways to get 200 dollars, with given denominations
def prob31():
    numways = 0
    cursum = 0
    for one in range(0, 201):
        cursum += 1*one
        for two in range(0, 101):
            cursum += 2*two
            if(cursum > 200):
                cursum -= 2*two
                break
            for five in range(0,41):
                cursum += 5*five
                if(cursum > 200):
                    cursum -= 5*five
                    break
                for ten in range(0, 21):
                    cursum += 10*ten
                    if(cursum > 200):
                        cursum -= 10*ten
                        break
                    for twenty in range(0, 11):
                        cursum += 20*twenty
                        if(cursum > 200):
                            cursum -= 20*twenty
                            break
                        for fifty in range(0, 5):
                            cursum += 50*fifty
                            if(cursum > 200):
                                cursum -= 50*fifty
                                break
                            for hundred in range(0, 3):
                                cursum += 100*hundred
                                if(cursum > 200):
                                    cursum -= 100*hundred
                                    break
                                for twohundred in range(0, 2):
                                    cursum += 200*twohundred
                                    if (cursum == 200):
                                        numways += 1
                                    cursum -= 200*twohundred
                                cursum -= 100*hundred
                            cursum -= 50*fifty
                        cursum -= 20*twenty
                    cursum -= 10*ten
                cursum -= 5*five
            cursum -= 2*two
        cursum-= 1 * one
    return numways


newN = []
repeat = []
insert = []

#number of ways to get 200 dollars, with given denominations
#dynamic programming
def prob31b():
    numWays = 0
    curSum = 0

    #denominations
    values = [1, 2, 5, 10, 20, 50, 100, 200]

    # {2: [{1: 2}, {2:1}], 5: [{1: 1, 2: 2}, {5: 1}, {1: 3, 2: 1}]}
    # holds a list of unique unordered sequence of denominations per total sum
    dictWays = {}

    # {1: 4, 2: 4, 10: 1}
    # current set of used coins
    dictSequence = {}
    for value in values:
        dictSequence[value] = 0

    prob31help(dictSequence, 0, dictWays, values)

    print("insert: " + str(len(insert)) + ", repeat: " + str(len(repeat)) + ", new: " + str(len(newN)))

    return len(dictWays[200])


def prob31help(curSequence, curSum, dictWays, values):
    if curSum < 60:
        for curValue in values:
            newSum = curSum + curValue
            newSequence = dict(curSequence)
            newSequence[curValue] += 1

            if newSum in dictWays:
                #check for duplicates
                repeated = False
                for curSet in dictWays[newSum]:
                    innerRepeat = True
                    for value in values:
                        if newSequence[value] != curSet[value]:
                            innerRepeat = False
                            break
                    if innerRepeat:
                        repeated = True
                        repeat.append(1)
                        break
                if not repeated:
                    dictWays[newSum].append(newSequence)
                    prob31help(newSequence, newSum, dictWays, values)
                    insert.append(1)
            else:
                dictWays[newSum] = [newSequence]
                newN.append(1)
                prob31help(newSequence, newSum, dictWays, values)



#how to get up 100 steps given you can go up 1 or 2 steps each time
def stepper():
    stepsdict = {}
    return stepsfn(0, stepsdict, 100)

def stepsfn(step, stepsdict, numsteps):
    if step < numsteps:
        if step in stepsdict:
            return stepsdict[step]
        else:
            stepsdict[step] = stepsfn(step + 1, stepsdict, numsteps) + stepsfn(step + 2, stepsdict, numsteps)
            return stepsdict[step]
    elif step == numsteps:
        return 1
    elif step > numsteps:
        return 0





