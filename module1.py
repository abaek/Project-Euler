#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Andy
#
# Created:     22-12-2013
# Copyright:   (c) Andy 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()

#Euler 1

"""sum = 0

for i in range(3, 1000, 3):
    sum += i

for i in range(5, 1000, 5):
    sum += i

for i in range(15, 1000, 15):
    sum -= i

print sum"""


#Euler 4

"""def palindrome6(x):
    num = str(x)
    if (len(num) == 6
            and num[5] == num[0]
            and num[4] == num[1]
            and num[3] == num[2]):
                return True
    else:
         return False

cond = True
largest = 1
num1 = 999
num2 = 999

while (cond):
    x = num1 * num2

    if palindrome6(x) and x > largest:
        largest = x
        print largest

    if (not(num1 == 100)):
        num1 -= 1
    elif (not(num2 == 100)):
        num1 = 999
        num2 -= 1
    else:
        cond = False"""


#Euler 8

"""product = 0
x = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

for i in range(0, 996):
    current = int(x[i])*int(x[i+1])*int(x[i+2])*int(x[i+3])*int(x[i+4])
    if current > product:
        product = current
        print product

print product"""


#Euler 9

"""a = 1
b = 2
c = 997


while not(a**2 + b**2 == c**2):
    if c > b:
        c -= 1
        b += 1
    else:
        a += 1
        b = a + 1
        c = 1000 - a - b"""


#Euler 11

"""def prob11():
    nestedli = convFile(open("C:\Users\Andy\Documents\\1A\Programming\prob11.txt", "r"))

    greatest = 0
    #checks rows
    for i in nestedli:
        if accross(i) > greatest:
            greatest = accross(i)

    #checks columns
    for x in range(len(nestedli[0])):
        currentCol = [i[x] for i in nestedli]#set comprehension (aka map)
        if accross(currentCol) > greatest:
            greatest = accross(currentCol)

    #checks diagonals
    #top right
    def topright(grid, greatest):
        for x in range(16):
            row = [grid[i][x+i] for i in range(20 - x)]
            if accross(row) > greatest:
                greatest = accross(row)
        return greatest

    #top left
    def topleft(grid, greatest):
        for x in range(3, 20):
            row = [grid[i][x-i] for i in range(x+1)]
            if accross(row) > greatest:
                greatest = accross(row)
        return greatest

    greatest = topright(nestedli, greatest)
    greatest = topleft(nestedli, greatest)

    #reverse list vertically
    nestedli = nestedli[::-1]

    greatest = topright(nestedli, greatest)
    greatest = topleft(nestedli, greatest)

    return greatest


#convert file to nested list of numbers
def convFile(x):
    masterli = []
    for strline in x:
        numline = [int(a) for a in strline.split()] #list comprehension (aka map)
        masterli.append(numline)
    return masterli

#Gets largest 4 consecutive number product in list
def accross(row):
    greatest = 0
    for x in range(len(row) - 3):
        product = 1
        for i in range(x, x+4):
            product *= row[i]
        if product > greatest:
            greatest = product
    return greatest"""



#Euler 13


"""x = 37107287533902102798797998220837590246510135740250
46376937677490009712648124896970078050417018260538
74324986199524741059474233309513058123726617309629
91942213363574161572522430563301811072406154908250
23067588207539346171171980310421047513778063246676
89261670696623633820136378418383684178734361726757
28112879812849979408065481931592621691275889832738
44274228917432520321923589422876796487670272189318
47451445736001306439091167216856844588711603153276
70386486105843025439939619828917593665686757934951
62176457141856560629502157223196586755079324193331
64906352462741904929101432445813822663347944758178
92575867718337217661963751590579239728245598838407
58203565325359399008402633568948830189458628227828
80181199384826282014278194139940567587151170094390
35398664372827112653829987240784473053190104293586
86515506006295864861532075273371959191420517255829
71693888707715466499115593487603532921714970056938
54370070576826684624621495650076471787294438377604
53282654108756828443191190634694037855217779295145
36123272525000296071075082563815656710885258350721
45876576172410976447339110607218265236877223636045
17423706905851860660448207621209813287860733969412
81142660418086830619328460811191061556940512689692
51934325451728388641918047049293215058642563049483
62467221648435076201727918039944693004732956340691
15732444386908125794514089057706229429197107928209
55037687525678773091862540744969844508330393682126
18336384825330154686196124348767681297534375946515
80386287592878490201521685554828717201219257766954
78182833757993103614740356856449095527097864797581
16726320100436897842553539920931837441497806860984
48403098129077791799088218795327364475675590848030
87086987551392711854517078544161852424320693150332
59959406895756536782107074926966537676326235447210
69793950679652694742597709739166693763042633987085
41052684708299085211399427365734116182760315001271
65378607361501080857009149939512557028198746004375
35829035317434717326932123578154982629742552737307
94953759765105305946966067683156574377167401875275
88902802571733229619176668713819931811048770190271
25267680276078003013678680992525463401061632866526
36270218540497705585629946580636237993140746255962
24074486908231174977792365466257246923322810917141
91430288197103288597806669760892938638285025333403
34413065578016127815921815005561868836468420090470
23053081172816430487623791969842487255036638784583
11487696932154902810424020138335124462181441773470
63783299490636259666498587618221225225512486764533
67720186971698544312419572409913959008952310058822
95548255300263520781532296796249481641953868218774
76085327132285723110424803456124867697064507995236
37774242535411291684276865538926205024910326572967
23701913275725675285653248258265463092207058596522
29798860272258331913126375147341994889534765745501
18495701454879288984856827726077713721403798879715
38298203783031473527721580348144513491373226651381
34829543829199918180278916522431027392251122869539
40957953066405232632538044100059654939159879593635
29746152185502371307642255121183693803580388584903
41698116222072977186158236678424689157993532961922
62467957194401269043877107275048102390895523597457
23189706772547915061505504953922979530901129967519
86188088225875314529584099251203829009407770775672
11306739708304724483816533873502340845647058077308
82959174767140363198008187129011875491310547126581
97623331044818386269515456334926366572897563400500
42846280183517070527831839425882145521227251250327
55121603546981200581762165212827652751691296897789
32238195734329339946437501907836945765883352399886
75506164965184775180738168837861091527357929701337
62177842752192623401942399639168044983993173312731
32924185707147349566916674687634660915035914677504
99518671430235219628894890102423325116913619626622
73267460800591547471830798392868535206946944540724
76841822524674417161514036427982273348055556214818
97142617910342598647204516893989422179826088076852
87783646182799346313767754307809363333018982642090
10848802521674670883215120185883543223812876952786
71329612474782464538636993009049310363619763878039
62184073572399794223406235393808339651327408011116
66627891981488087797941876876144230030984490851411
60661826293682836764744779239180335110989069790714
85786944089552990653640447425576083659976645795096
66024396409905389607120198219976047599490197230297
64913982680032973156037120041377903785566085089252
16730939319872750275468906903707539413042652315011
94809377245048795150954100921645863754710598436791
78639167021187492431995700641917969777599028300699
15368713711936614952811305876380278410754449733078
40789923115535562561142322423255033685442488917353
44889911501440648020369068063960672322193204149535
41503128880339536053299340368006977710650566631954
81234880673210146739058568557934581403627822703280
82616570773948327592232845941706525094512325230608
22918802058777319719839450180888072429661980811197
77158542502016545090413245809786882778948721859617
72107838435069186155435662884062257473692284509516
20849603980134001723930671666823555245252804609722
53503534226472524250874054075591789781264330331690

sum = 0

for i in range(0, 51 * 100, 51):
    sum += int(x[i:i+50])
    print sum

"""

#Euler 14

"""def collatz(x):
    if x%2 == 0:
        return x / 2
    else:
        return 3*x + 1

def collatzlen(x):
    return collatzlenhelp(x, 1)

def collatzlenhelp(x, n):
    if x == 1:
        return n
    elif x%2 == 0:
        return collatzlenhelp(x/2, n+1)
    else:
        return collatzlenhelp(3*x + 1, n+1)

largestLength = 0
largestNum = 0

for i in range(999999, 0, -2):
    if collatzlen(i)>largestLength:
        largestLength  = collatzlen(i)
        largestNum = i
    else:
        pass"""


#Euler 17

"""upTo9 = 3*3 + 4*3 + 5*3
upTo19 = upTo9 + len('tenElevenTwelveThirteenFourteenFifteenSixteenSeventeenEighteenNineteen')
upTo99 = upTo19 + (10 * len('twentyThirtyFortyFiftySixtySeventyEightyNinety')) + (8 * upTo9)
upTo999 = upTo99 + (len('hundredand') * 99 * 9) + (upTo9 * 100) + (len('hundred') * 9) + (upTo99 * 9)
upTo1000 = upTo999 + len('onethousand')
print upTo1000"""


#Euler 18

"""def prob18():

    #convert file to nested list of numbers
    def convFile(x):
        masterli = []
        for strline in x:
            line = strline.split()
            numline = []
            for i in line:
                numline.append(int(i))
            masterli.append(numline)
        return masterli

    tree = convFile(open("C:\Users\Andy\Documents\\1A\Programming\prob18.txt", "r"))

    def takesum(row, pos, total):
        if row < len(tree):
            return max(takesum(row+1, pos, total+tree[row][pos]), takesum(row+1, pos+1, total+tree[row][pos]))
        else:
            return total

    return takesum(0, 0, 0)"""


#Euler 19

"""numSun = 0
firstdays = []
daycounter = 1
sundays = []

for year in range(1901, 2001):
    for month in range(1, 13):
        firstdays.append(daycounter)
        if month == 1 or month ==3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            daycounter += 31
        elif month == 4 or month == 6 or month == 9 or month == 11:
             daycounter += 30
        elif year%4 == 0 and (not(year%100 == 0) or year%400 == 0):
            daycounter += 29
        else:
            daycounter += 28

for day in range(1, 36496, 7):
    sundays.append(day)

numSun = len(list(set(firstdays) & set(sundays)))

print numSun"""


#Euler 20

"""product = 1
sum = 0

for i in range(1, 101):
    product *= i

for x in range(0, len(str(product))):
    sum += int(str(product)[x])
    print sum"""


#Euler 21

"""def factors(x):
    factors = []
    for i in range(1, x/2 + 1):
        if x%i == 0:
            factors.append(i)
    return factors

amicable = []

for i in range(2, 10000):
    if i == sum(factors(sum(factors(i)))) and not(i == sum(factors(i))):
        amicable.append(i)

print sum(amicable)"""


#Euler 22

"""def prob22():
    names = open("C:\Users\Andy\Documents\\1A\Programming\prob22.txt", "r")
    for line in names:
        lonames = line.split(",")
    listofNames= [name[1:len(name)-1] for name in lonames]

    points = scoreDictionary()
    sortedNames = []

    sortedNames = mergesort(listofNames) #choose sort

    sum = 0
    for i in range(len(sortedNames)):
        sum += (scoreWord(sortedNames[i], points)*(i+1))

    return sum
    #return sortedNames

#merge sort
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

#insertion sort
def insertion(x, sortedWords):
    if not sortedWords:
        sortedWords.append(x)
    i = 0
    while i < len(sortedWords) and sortedWords[i] < x :
        i += 1
    sortedWords.insert(i, x)

def sort(listofWords):
    newlist = []
    for i in listofWords:
        insertion(i, newlist)
    return newlist

#quicksort
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
    return sum"""


#Euler 23

"""def propDiv(x):
    Div = []
    for i in range(1, x/2 + 1):
        if x%i == 0:
            Div.append(i)
    return Div

def abundant(x):
    if sum(propDiv(x)) > x:
        return True
    else:
        return False

def listAbundant():
    loa = []
    for i in range(1, 29124):
        if abundant(i):
            loa.append(i)
    return loa

def prob23():
    loa = listAbundant()
    sums = set([])
    for elem1 in loa:
        for elem2 in loa:
            if elem1 + elem2 < 28124:
                sums.add(elem1+elem2)
    total = (1 +28123)*(28123/2) - sum(sums)
    return total"""


#Euler 24:



def prob24():
    listofperm = []
    Digitfn(10, range(10), 0, listofperm)
    return listofperm[999999]

def Digitfn(pos, curSet, summ, listofperm):
    if pos == 1:
        num = curSet[0]
        summ += num
        listofperm.append(summ)
        summ -= num
    else:
        for a in range(pos):
            num = curSet[a]
            set2 = curSet[:]
            set2.pop(a)
            summ += num*(10**(pos-1))
            Digitfn(pos - 1, set2, summ, listofperm)
            summ -= num*(10**(pos-1))


#Euler 25
"""def Fib(termNum):
    term1, term2 = 1, 1
    termNum -= 2
    while termNum > 0:
        term3 = term1 + term2
        term1 = term2
        term2 = term3
        termNum -=1
    return term2

def prob25():
    i = 1
    while len(str(Fib(i)))<1000:
        i+=1
    return i"""


#Euler 26

'''def prob26():
    longest = 0
    for i in range(1, 1000):
        length = len(str(1.0/i))'''


#Euler 27

def prime(x):
    isPrime = True
    for div in range(2, x/2+1):
        if x%div == 0:
            isPrime = False
            break
    return isPrime


def listPrimes(x):
    listP = []
    for div in range(2, x/2+1):
        if prime(div):
            listP.append(div)
    return listP

def prime1000(x, lst):
    isPrime = True
    for elem in lst:
        if x%elem == 0:
            isPrime = False
    return isPrime

def prob27():
    curNumPrimes = 0
    curProduct = 0
    primes = listPrimes(501)
    num1 = 0
    num2 = 0

    for a in range(-999, 1000):
        for b in range(-999, 1000):
            n = 0
            stillPrime = True
            while stillPrime:
                quad = n**2+ n*a + b
                if prime1000(quad, primes):
                    n+=1
                else:
                    if n>=curNumPrimes:
                        curNumPrimes = n
                        curProduct = a*b
                        num1 = a
                        num2 = b
                    stillPrime = False

    print curProduct
    print num1
    print num2
    print curNumPrimes











