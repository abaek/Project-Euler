#-------------------------------------------------------------------------------
# Author:      Andy Baek
# Created:     20-12-2013
# Copyright:   (c) Andy Baek 2014
# Questions:   http://projecteuler.net/
#-------------------------------------------------------------------------------
from Useful_Functions import *

"""
1. Find the sum of all multiples of 3 or 5, but not both
"""
def prob1():
    sum = 0
    for i in range(3, 1000, 3):
        sum += i
    for i in range(5, 1000, 5):
        sum += i
    for i in range(15, 1000, 15):
        sum -= i
    return sum

"""
2. Find the sum of the even Fibonacci numbers under four million
"""
def prob2():
    maxTerm = 4000000
    t1 = 1
    t2 = 2
    sumEven = 2
    while True:
        temp = t2
        t2 += t1
        t1 = temp
        if t2 > maxTerm:
            break
        if t2%2 == 0:
            sumEven += t2
    return sumEven

"""
3. What is the largest prime factor of the number 600851475143 ?
"""
def prob3():
    number= 600851475143
    curNum = 2
    while True:
        maxFactor = (int(number**(1/2.0)))
        if curNum > maxFactor:
            break
        if isPrime(curNum):
            while True:
                if number%curNum == 0:
                    number /= curNum
                else:
                    break
        curNum+=1
    return number

"""
4. Find the largest palindrome that is a product of two 3-digit integers
"""
def prob4():
    largest = 0
    for num1 in range(999, 99, -1):
        if num1*999 < largest:
            break
        for num2 in range(999, 99, -1):
            product = num1*num2
            if product <= largest:
                break
            if palindrome(product):
                num1
                largest = product
    return largest, iterations

def palindrome(x):
    origStr = str(x)
    reverseStr = ''.join(curChar for curChar in origStr[::-1])
    if int(reverseStr) == x:
        return True
    else:
        return False

"""
5. What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
"""
def prob5():
    maxNum = 20
    primeFactors = {}
    factors = findPrimes(maxNum)
    for factor in factors:
        primeFactors[factor] = 1
        count = 2
        while factor**count <= maxNum:
            primeFactors[factor] += 1
            count+=1
    num = 1
    for factor in primeFactors.iterkeys():
        num *= factor**primeFactors[factor]
    return num

"""
6. Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.
"""
def prob6():
    sumofSquares = 0
    squareofSum = 0
    sum = 0
    for i in range(1,101):
        sum+=i
        sumofSquares += i**2
    squareofSum = sum **2
    return squareofSum - sumofSquares

"""
7. What is the 10 001st prime number?
"""
def prob7():
    numPrimes = 0
    primes = []
    i=2
    while (numPrimes < 10001):
        isPrime = True
        maxFactor = i**(1/2.0)
        for prime in primes:
            if i%prime == 0:
                isPrime = False
                break
            if prime > maxFactor:
                break
        if isPrime:
            primes.append(i)
            numPrimes += 1
        i+=1
    return primes[-1]

"""
8. Find the largest product of 5 consecutive digits in the 1000 digit number:
    7316717653133062491922511967442657474235534919493496983520312
    77450632623957831801698480186947885184385861560789112949495459
    ...
    98315520005593572972571636269561882670428252483600823257530420
    752963450
"""
def prob8():
    numStr = convNumStr(open("C:\Users\Andy\Documents\GitHub\Project-Euler\Text_Files", "r"))
    largest = 0
    for i in range(0, len(numStr)-4):
        current = int(numStr[i])*int(numStr[i+1])*int(numStr[i+2])*int(numStr[i+3])*int(numStr[i+4])
        if current > largest:
            largest = current
    return largest

#converts file containing number broken into lines into a single string
def convNumStr(file):
    lstNum = []
    numStr = ""
    for line in file:
        lstNum.append(line)
    #skips every \n in ever line except the last line
    lastLine = len(lstNum) -1
    for line in range(lastLine + 1):
        if line == lastLine:
            numStr += lstNum[line]
        else:
            numStr += lstNum[line][:-1]
    return numStr

"""
9. Find the Pythagorean triplet (a^2 + b^2 = c^2) where a+b+c = 1000
"""
def prob9():
    a = 1
    b = 2
    c = 997

    while not(a**2 + b**2 == c**2):
        if c > b:
            c -= 1
            b += 1
        else:
            a += 1
            b = a + 1
            c = 1000 - a - b
    return a*b*c
