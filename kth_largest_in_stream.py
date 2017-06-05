# http://practice.geeksforgeeks.org/problems/kth-largest-element-in-a-stream/0

class KthHelper:
    def __init__(self, k):
        self.k = k
        self.number_list = []

    def getKth(self, num):
        length = len(self.number_list)
        idx = length // 2
        left = 0
        right = length
        while True:
            if left >= right:
                self.number_list.insert(idx, num)
                break
            element = self.number_list[idx]
            if element > num:
                left = idx+1
            else:
                right = idx
            idx = (left + right) // 2
        if len(self.number_list) >= self.k:
            self.prev_kth = self.number_list[k-1]
            return self.prev_kth
        else:
            return -1

if __name__ == "__main__":
    num_cases = int(input())
    results = []
    for _ in range(num_cases):
        input_string = input()
        input_list = input_string.split(" ")
        k = int(input_list[0])
        n = int(input_list[1])
        input_string = input()
        result = []
        kth = KthHelper(k)
        splitted = input_string.split(" ")
        for i in range(n):
            result.append(kth.getKth(int(splitted[i])))
        results.append(result)

    for result in results:
        print_str = ""
        for num in result:
            print_str += str(num)
            print_str += " "
        print(print_str[:-1])

