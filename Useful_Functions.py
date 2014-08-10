#-------------------------------------------------------------------------------
# Author:      Andy Baek
# Created:     20-12-2013
# Copyright:   (c) Andy Baek 2014
#-------------------------------------------------------------------------------

def isPrime(num):
    if num==2 or num==3:
        return True
    if num==1 or num%2==0 or num%3==0:
        return False
    else:
        maxFactor = int(num**(0.5))
        for i in range(5, maxFactor+1, 6):
            if num%i == 0 or num%(i+2)==0:
                return False
                break
    return True

def findPrimes(maxNum):
    primes = []
    for i in range(2, maxNum+1):
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
    return primes

def findPrimeFactorization(num):
    factors = {}
    curNum = 2
    while True:
        maxFactor = int(num**0.5)
        if curNum > maxFactor:
            if curNum in factors:
                factors[num] += 1
            else:
                factors[num] =1
            break
        if isPrime(curNum):
            first = True
            while True:
                if num%curNum == 0:
                    if first:
                        factors[curNum] = 1
                        first = False
                    else:
                        factors[curNum] += 1
                    num /= curNum
                else:
                    break
        curNum+=1
    return factors