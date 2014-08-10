#-------------------------------------------------------------------------------
# Author:      Andy Baek
# Created:     09-08-2014
# Copyright:   (c) Andy Baek 2014
#-------------------------------------------------------------------------------

"""
26. Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
    1/7	= 	0.(142857) -> 6-digit recurring cycle
"""
#not finished
from decimal import *
def prob26():
    getcontext().prec = 10
    digitDict = {}
    maxCycleLength = 0
    maxNum = 0
    for i in range(10):
        digitDict[i] = False
    for i in range(2, 1000):
        quotient = Decimal(1) / Decimal(i)
        decimalDigits = str(quotient).split('.')[1]

        cycleLength = 0
        for digit in decimalDigits:
            if digitDict[int(digit)]:
                break
            cycleLength+=1
            digitDict[int(digit)] = True
        if cycleLength > maxCycleLength:
            print(i)
            maxCycleLength=cycleLength
            maxNum = i
        for j in range(10):
            digitDict[j] = False
    return maxNum


"""
29. Find the number of unique powers with base and exponent ranging from 2-100
"""
def prob29():
    setpowers = set()
    for a in range(2, 101):
        for b in range(2, 101):
            setpowers.add(pow(a, b))
    return len(setpowers)


"""
30. Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
def prob30c():
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

"""
31. Find the number of ways to get 200p dollars, with given coin denominations: 1p, 2p, 5p, 10p, 20p, 50p, 100p and 200p.
"""
#dynamic programming: table[i][j] represents number of ways to get
#j dollars using the first i+1 coins
def prob31():
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    target = 200
    table = [0]*len(coins)
    table[0] = [1]*(target+1)
    for i in range(1, len(coins)):
        table[i] = [0]*(target+1)
    for coinPos in range(1, len(coins)):
        lastCoin = coins[coinPos]
        for index in range(target+1):
            if index < lastCoin:
                table[coinPos][index] = table[coinPos-1][index]
            else:
                table[coinPos][index] = table[coinPos-1][index] + table[coinPos][index-lastCoin]
    print(table)
    return table[-1][-1]


