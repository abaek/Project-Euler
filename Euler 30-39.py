#-------------------------------------------------------------------------------
# Author:      Andy Baek
# Created:     21-08-2014
# Copyright:   (c) Andy Baek 2014
# Questions:   http://projecteuler.net/
#-------------------------------------------------------------------------------
from Useful_Functions import *
"""
30. Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
def prob30():
    #determine max possible digits
    maxPossibleDigits = 1
    maxPerDigit = 9**5
    while(True):
        if(maxPerDigit*maxPossibleDigits < 10**(maxPossibleDigits-1)):
            maxPossibleDigits -= 1
            break
        maxPossibleDigits+=1
    #remove constant calculation
    fifthPowers = {}
    for i in range(10):
        fifthPowers[i] = i**5
    #iterate through all numbers under 7 digits
    result = 0
    for numDigits in range(2, maxPossibleDigits+1):
        print numDigits
        for num in range(10**(numDigits-1), (10**numDigits)+1):
            origNum = num
            sumPowers = 0
            for i in range(numDigits):
                sumPowers += fifthPowers[num%10]
                num /= 10
            if sumPowers == origNum:
                result += origNum
                print result
    return result

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

"""
32. Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
    ex: 39 ? 186 = 7254
    An n-digit number is pandigital if it makes use of all the digits 1 to n exactly once (ex: 15234)
"""
def prob32():
    pandigitals = set()
    result = 0
    isPandigital = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    #2-digit times 3-digit
    for num1 in range(10, 100):
        for num2 in range(100, 1000):
            product = num1*num2
            if product > 9999:
                break
            numString = str(num1) + str(num2) + str(product)
            if sorted(numString) == isPandigital:
                if not (product in pandigitals):
                    pandigitals.add(product)
                    result += product
                    print product, num1, num2
    #1-digit times 4-digit
    for num1 in range(1, 10):
        for num2 in range(1000, 10000):
            product = num1*num2
            if product > 9999:
                break
            numString = str(num1) + str(num2) + str(product)
            if sorted(numString) == isPandigital:
                if not (product in pandigitals):
                    pandigitals.add(product)
                    result += product
                    print product, num1, num2
    return result














