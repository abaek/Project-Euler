#-------------------------------------------------------------------------------
# Author:      Andy Baek
# Created:     10-08-2014
# Copyright:   (c) Andy Baek 2014
# Questions:   http://projecteuler.net/
#-------------------------------------------------------------------------------
from Useful_Functions import *

"""
20. Calculate the sum of the digits in the number 100!
"""
def prob20():
    product = 1
    sum = 0
    for i in range(1, 101):
        product *= i
    for x in range(0, len(str(product))):
        sum += int(str(product)[x])
    return sum

"""
21. Evaluate the sum of all amicable numbers under 10000
Let d(n) be defined as the sum of proper divisors of n
If d(a) = b and d(b) = a, where a != b, then each of a and b are called amicable numbers.
"""
def prob21():
    amicable = []
    for i in range(2, 10000):
        sumFactors = sum(properDivisors(i))
        if not(i == sumFactors) and i == sum(properDivisors(sumFactors)[:-1]):
            amicable.append(i)
    return sum(amicable)

"""
22. Sorts 5000 names lexographically then adds their values
"""
def prob22():
    names = open("C:\Users\Andy\Documents\GitHub\Project-Euler\Text_Files\prob22.txt", "r")
    for line in names:
        lonames = line.split(",")
    listofNames= [name[1:len(name)-1] for name in lonames]
    points = scoreDictionary()
    sortedNames = []
    sortedNames = sort(listofNames)
    sum = 0
    for i in range(len(sortedNames)):
        sum += (scoreWord(sortedNames[i], points)*(i+1))
    return sum

def scoreDictionary():
    points = {}
    alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    for i in range(26):
        points[alphabet[i]] = i+1
    return points

def scoreWord(word, points):
    sum = 0
    for i in list(word):
        sum += points[i]
    return sum

"""
23. Returns the sum of all integers which cannot be written as a sum of two abundant numbers under 28124
A number is abundant if the sum of its proper divisors are greater than the number itself
"""
def prob23():
    loa = listAbundant()
    sums = set([])
    for elem1 in loa:
        for elem2 in loa:
            curSum = elem1 + elem2
            if curSum < 28124:
                sums.add(curSum)
    total = (1 +28123)*(28123/2) - sum(sums) #arithmetic series
    return total

def listAbundant():
    loa = []
    for i in range(1, 28124):
        if abundant(i):
            loa.append(i)
    return loa

def abundant(x):
    if sum(properDivisors(x)) > x:
        return True
    else:
        return False

"""
24. Returns the millionth lexographic permutation of the digits {0...9}
(2783915460)
"""
#determine digits one by one by counting permutations
def prob24():
    desiredPos = 999999
    currentFactorial = 9
    solution = 0
    digitsLeft = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(10):
        factorialValue = factorial(currentFactorial)
        numTimes = desiredPos/factorialValue
        solution += digitsLeft[numTimes] * (10**currentFactorial)
        digitsLeft.pop(numTimes)
        desiredPos -= numTimes* factorialValue
        currentFactorial -= 1
    return solution

def factorial(n):
    result= 1
    for i in range(1, n+1):
        result *= i
    return result

"""
25. Returns the first term in the Fibonacci sequence to contain 1000 digits
"""
def prob25():
    term1, term2 = 1, 1
    index = 2
    divisor = 10**999
    while term2/divisor == 0:
        temp = term2
        term2 += term1
        term1 = temp
        index+=1
    return index

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
27. Find the product of the coefficients, a and b, for the quadratic expression:
    n^2 + an + b, where |a| < 1000 and |b| < 1000
    that produces the maximum number of primes for consecutive values of n, starting with n = 0.
"""
def prob27():
    maxPrimes = 0
    result = 0
    for a in range(-999, 1000, 1):
        for b in range(-999, 1000, 1):
            n = 0
            while True:
                quadratic = n**2 + a*n + b
                if quadratic > 1 and isPrime(quadratic):
                    n+=1
                else:
                    break
            if n > maxPrimes:
                result = a*b
                maxPrimes = n
    return result

"""
28. What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way
    as this 5 by 5 spiral:  21 22 23 24 25
                            20  7  8  9 10
                            19  6  1  2 11
                            18  5  4  3 12
                            17 16 15 14 13
"""
def prob28():
    result = 1
    currentNum = 1
    spiralDiameter = 3
    while spiralDiameter <= 1001:
        for i in range(4):
            currentNum += spiralDiameter-1
            result += currentNum
        spiralDiameter += 2
    return result

"""
29. Find the number of unique powers with base and exponent ranging from 2-100
"""
def prob29():
    setpowers = set()
    for a in range(2, 101):
        for b in range(2, 101):
            setpowers.add(pow(a, b))
    return len(setpowers)