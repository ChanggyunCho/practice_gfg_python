# Sorting Elements of an Array by Frequency
# http://practice.geeksforgeeks.org/problems/sorting-elements-of-an-array-by-frequency/0
import functools

def comparator(x, y):
    keyX = x[1]
    keyY = y[1]

    if keyX == keyY:
        return y[0] - x[0]
    else:
        return keyX - keyY

class Algorithm:
    def __init__(self):
        self.numberDictionary = {}

    def addNumber(self, value):
        if value in self.numberDictionary:
            self.numberDictionary[value] += 1
        else:
            self.numberDictionary[value] = 1
    
    def getResult(self):
        sortedList = sorted(self.numberDictionary.items(), key=functools.cmp_to_key(comparator), reverse=True)

        ret = ""
        for elem in sortedList:
            value = elem[0]
            repeat = elem[1]
            numberString = "%d "%(value) * repeat
            ret += numberString
        # tempList = []
        # frequency = 0
        # for elem in sortedList:

        return ret

if __name__ == "__main__":
    no_cases = int(input())
    results = []
    for _ in range(no_cases):
        n = int(input())
        input_string = input()
        splitted = input_string.split(" ")
        algorithm = Algorithm()
        for i in range(n):
            algorithm.addNumber(int(splitted[i]))
        results.append(algorithm.getResult())

    for result in results:
        print(result)