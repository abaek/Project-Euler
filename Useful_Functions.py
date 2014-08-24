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

def findFactors(num):
    factors = set()
    maxFactor = int(num**0.5)
    for i in range(1, maxFactor+1):
        if num%i == 0:
            factors.add(i)
            factors.add(num/i)
    factorsList = list(factors)
    factorsList.sort()
    return factorsList

def properDivisors(num):
    factors = set([1])
    maxFactor = int(num**0.5)
    for i in range(2, maxFactor+1):
        if num%i == 0:
            factors.add(i)
            factors.add(num/i)
    factorsList = list(factors)
    return factorsList

#Option 1: merge sort
def mergeNoRecurse(l1, l2):
    second = 0
    first = 0
    newlist = []
    while True:
        if second >= len(l2):
            newlist.extend(l1[first:])
            break
        elif first >= len(l1):
            newlist.extend(l2[second:])
            break
        elif l1[first]<l2[second]:
            newlist.append(l1[first])
            first += 1
        elif l1[first]>=l2[second]:
            newlist.append(l2[second])
            second += 1
    return newlist

def mergesort(lst):
    if not lst:
        return []
    elif len(lst) == 1:
        return lst
    else:
        return mergeNoRecurse(mergesort(lst[:len(lst)/2]), mergesort(lst[len(lst)/2:]))


#Option 2: quicksort
def choosePivot(lst):
    lower = []
    higher = []
    pivot = lst[0]
    for i in lst[1:]:
        if i > pivot:
            higher.append(i)
        else:
            lower.append(i)
    newlist = quicksort(lower)
    newlist.append(pivot)
    newlist.extend(quicksort(higher))
    return newlist

def quicksort(lst):
    if not lst:
        return []
    else:
        newlist = choosePivot(lst)
        return newlist