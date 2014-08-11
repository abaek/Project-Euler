#-------------------------------------------------------------------------------
# Author:      Andy Baek
# Created:     20-12-2013
# Copyright:   (c) Andy Baek 2014
# Questions:   http://projecteuler.net/
#-------------------------------------------------------------------------------
from Useful_Functions import *

"""
10. Find the sum of all the primes below two million.
"""
def prob10():
    primes = findPrimes(2000000)
    return sum(primes)

"""
11. Returns the largest product of 4 adjacent numbers in a 20x20 grid (vertical, horizontal, diagonal)
"""
def prob11():
    nestedli = []
    file = open("C:\Users\Andy\Documents\GitHub\Project-Euler\Text_Files\prob11.txt", "r")
    for strline in file:
        numline = [int(a) for a in strline.split()]
        nestedli.append(numline)
    greatest = 0
    #checks rows
    for row in nestedli:
        curProduct = accross(row)
        if curProduct > greatest:
            greatest = curProduct
    #checks columns
    for pos in range(len(nestedli[0])):
        currentCol = [row[pos] for row in nestedli]
        curProduct = accross(currentCol)
        if  curProduct > greatest:
            greatest = curProduct
    #checks diagonals
    #top right triangle
    def topright(grid, greatest):
        for x in range(16):
            row = [grid[i][x+i] for i in range(20 - x)]
            if accross(row) > greatest:
                greatest = accross(row)
        return greatest
    #top left triangle
    def topleft(grid, greatest):
        for x in range(3, 20):
            row = [grid[i][x-i] for i in range(x+1)]
            if accross(row) > greatest:
                greatest = accross(row)
        return greatest
    greatest = topright(nestedli, greatest) #top right
    greatest = topleft(nestedli, greatest) #top left
    #reverse list vertically
    nestedli = nestedli[::-1]
    greatest = topright(nestedli, greatest) #bottom right
    greatest = topleft(nestedli, greatest) #bottom left
    return greatest

#Gets largest 4 consecutive number product in list
def accross(row):
    greatest = 0
    for x in range(len(row) - 3):
        product = 1
        for i in range(x, x+4):
            product *= row[i]
        if product > greatest:
            greatest = product
    return greatest

"""
12. What is the value of the first triangle number to have over five hundred divisors?
Ex: The 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28
"""
def prob12():
    number = 1
    increment = 2
    while(True):
        length = numFactors(number)
        if length > 100:
            print length, number
        if length > 500:
            break
        number+=increment
        increment+=1
    return number

def numFactors(num):
    numFactors = 0
    maxFactor = int(num**0.5)
    for i in range(1, maxFactor):
        if num%i == 0:
            numFactors += 2
    if num == maxFactor**2:
        numFactors += 1
    return numFactors

"""
13. Find the first 10 digits of a sum of 100 fifty digit numbers
"""
def prob13():
    file = open("C:\Users\Andy\Documents\GitHub\Project-Euler\Text_Files\prob13.txt", "r")
    listNum = [line for line in file]
    #skips \n character in each line except last line
    filteredList = [listNum[lineNum][:-1] for lineNum in range(len(listNum) - 1)]
    filteredList.append(listNum[-1])
    sum = 0
    for num in filteredList:
        sum += int(num)
    return int(str(sum)[:10])

"""
14. Return the longest collatz sequence with starting term up to one million
n -> n/2 (n is even)
n -> 3n + 1 (n is odd)
"""
def prob14():
    visited = dict()
    visited[1] = 0
    longestSequence = 0
    startingNum = 0
    for term in range(1, 1000000, 2):
        currentTermLength = findCollatzLength(term, visited)
        if currentTermLength > longestSequence:
            longestSequence = currentTermLength
            startingNum = term
    return startingNum, longestSequence

def findCollatzLength(term, visited):
    if term in visited:
        return visited[term]
    else:
        newTerm = term
        if term%2 == 0:
            newTerm /=2
        else:
            newTerm = term*3 + 1
        visited[term] = findCollatzLength(newTerm, visited) + 1
        return visited[term]

"""
15. Starting in the top left corner of a 20x20 grid, and only being able to move to
the right and down, how many routes are there to the bottom-right corner
"""
def prob15():
    paths = [[None for _ in range(21)] for _ in range(21)]
    paths[0] = [1]*21
    for i in range(21):
        paths[i][0] = 1
    for i in range(1, 21):
        for j in range(1, 21):
            paths[i][j] = paths[i-1][j] + paths[i][j-1]
    return paths[20][20]

"""
16. What is the sum of the digits of the number 2^1000?
"""
def prob16():
    num = 2**1000
    sumDigits = 0
    while num != 0:
        sumDigits += num%10
        num /= 10
    return sumDigits

"""
17. Return the length of the numbers up to 1000 in words
"""
def prob17():
    upTo9 = 3*3 + 4*3 + 5*3
    upTo19 = upTo9 + len('tenElevenTwelveThirteenFourteenFifteenSixteenSeventeenEighteenNineteen')
    upTo99 = upTo19 + (10 * len('twentyThirtyFortyFiftySixtySeventyEightyNinety')) + (8 * upTo9)
    upTo999 = upTo99 + (len('hundredand') * 99 * 9) + (upTo9 * 100) + (len('hundred') * 9) + (upTo99 * 9)
    upTo1000 = upTo999 + len('onethousand')
    return upTo1000

"""
18. Returns the largest sum working down a triangle (tree)
                        75
                       95 64
                      .......
      63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""
def prob18():
    #convert file to nested list of numbers
    file = open("C:\Users\Andy\Documents\GitHub\Project-Euler\Text_Files\prob18.txt", "r")
    tree = []
    for strline in file:
        line = strline.split()
        numline = []
        for i in line:
            numline.append(int(i))
        tree.append(numline)
    maxPerPosition = {}
    lastRow = len(tree)-1
    for i in range(len(tree[lastRow])):
        maxPerPosition[(lastRow, i)] = tree[lastRow][i]
    takesum((0, 0), tree, maxPerPosition)
    return maxPerPosition[(0, 0)]

def takesum(position, tree, visitedPositions):
    if position in visitedPositions:
        return visitedPositions[position]
    else:
        curValue = tree[position[0]][position[1]]
        visitedPositions[position] = max(curValue + takesum((position[0]+1, position[1]), tree, visitedPositions),
                                         curValue + takesum((position[0]+1, position[1]+1), tree, visitedPositions))
        return visitedPositions[position]

"""
67. Returns the largest sum working down a larger triangle (tree)
    59
    73 41
    ......
    23 33 44 81 80 92 ... 29 06 25 61 41 26 15 59 63 35
    (last row has 100 numbers)
"""
def prob67():
    #convert file to nested list of numbers
    file = open("C:\Users\Andy\Documents\GitHub\Project-Euler\Text_Files\prob67.txt", "r")
    tree = []
    for strline in file:
        line = strline.split()
        numline = []
        for i in line:
            numline.append(int(i))
        tree.append(numline)
    maxPerPosition = {}
    lastRow = len(tree)-1
    for i in range(len(tree[lastRow])):
        maxPerPosition[(lastRow, i)] = tree[lastRow][i]
    takesum((0, 0), tree, maxPerPosition)
    return maxPerPosition[(0, 0)]

"""
19. Returns the number of intersections of sundays and the first day of the month since 1900
"""
def prob19():
    numSun = 0
    firstDays = set()
    daycounter = 1
    months31 = set([1, 3, 5, 7, 8, 10, 12])
    for year in range(1901, 2001):
        for month in range(1, 13):
            firstDays.add(daycounter)
            if month in months31:
                daycounter += 31
            elif not month == 2:
                 daycounter += 30
            elif year%4 == 0 and (not(year%100 == 0) or year%400 == 0):
                daycounter += 29
            else:
                daycounter += 28
    for sunday in range(1, 36496, 7):
        if sunday in firstDays:
            numSun += 1
    return numSun
