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
    ex: 39 x 186 = 7254
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

"""
33. The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify
    it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

    We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

    There are exactly four non-trivial examples of this type of fraction, less than one in value,
    and containing two digits in the numerator and denominator.

    If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""
def prob33():
    numerator = 1
    denominator = 1
    nums = 0
    for commonDigit in range(1, 10):
        for topDigit in range(1, commonDigit+1):
            topNum = topDigit*10 + commonDigit
            if topDigit == commonDigit:
                for lowDigit in range(topDigit+1, 10):
                    lowNum = commonDigit*10 + lowDigit
                    if topNum*1.0/lowNum == topDigit*1.0/lowDigit:
                        numerator *= topNum
                        denominator *= lowNum
                        print topNum, lowNum
                        nums+=1
            else:
                for lowDigit in range(1, 10):
                    lowNum = commonDigit*10 + lowDigit
                    if topNum*1.0/lowNum == topDigit*1.0/lowDigit:
                        numerator *= topNum
                        denominator *= lowNum
                        print topNum, lowNum
                        nums+=1
    topFactors = findPrimeFactorization(numerator)
    lowFactors = findPrimeFactorization(denominator)
    result = 1
    for key in lowFactors:
        if key in topFactors:
            if topFactors[key] < lowFactors[key]:
                result *= key** (lowFactors[key]-topFactors[key])
        else:
            result *= key**lowFactors[key]
    return result

"""
34. Find the sum of all numbers which are equal to the sum of the factorial of their digits. (over 1 digit)
"""
def prob34():
    factorials = {0:1}
    for i in range(1, 10):
        factorials[i] = factorials[i-1]*i
    maxPerDigit = factorials[9]
    maxNumDigits = 1
    while 10**(maxNumDigits-1) <= maxPerDigit*maxNumDigits:
        maxNumDigits+=1
    maxNumDigits-=1
    result = 0
    for num in range(10, 10**maxNumDigits):
        origNum = num
        digitSum = 0
        while num != 0:
            digitSum += factorials[num%10]
            num /= 10
        if origNum == digitSum:
            result += origNum
            print origNum
    return result

"""
35. How many circular primes are there below one million?
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
"""
def prob35():
    digits = [1, 3, 7, 9]
    numCircularPrimes = 0
    for i in range(5):


"""
36. Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
"""
#Bit manipulation


"""
37. Find the sum of the only eleven primes (greater than 10) that are both truncatable from left to right and right to left.
ex: 3797 truncate from left: 3797, 797, 97, and 7. truncate from right: 3797, 379, 37, and 3.
"""










