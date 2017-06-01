# http://practice.geeksforgeeks.org/problems/find-median-in-a-stream/0

class MedianHelper:
    def __init__(self):
        # init heap
        self.array = []
        self.length = 0

    def insertValue(self, value):
        # insert value to array O(logn)
        idx = self.length // 2
        left = 0
        right = self.length
        while True:
            if left >= right:
                self.array.insert(idx, value)
                self.length += 1
                break
            element = self.array[idx]
            if element < value:
                # search right
                left = idx+1
                idx = (left + right) // 2
            else:
                # search left
                right = idx
                idx = (left + right) // 2

    def getMedian(self):
        index = self.length // 2
        if self.length % 2 == 1:
            median = self.array[index]
        else:
            median = (self.array[index-1] + self.array[index]) // 2
        return median

if __name__ == "__main__":
    num_inputs = int(input())
    results = []
    medianStream = MedianHelper()
    for i in range(num_inputs):
        value = int(input())
        medianStream.insertValue(value)
        results.append(medianStream.getMedian())
    
    for result in results:
        print(result)