# Largest Number formed from an Array
# http://practice.geeksforgeeks.org/problems/largest-number-formed-from-an-array/0
import functools

def comparator(x, y):
    xy = x + y
    yx = y + x
    return int(xy) - int(yx)

if __name__ == "__main__":
    # num_cases = int(1)
    num_cases = int(input())
    results = []
    for _ in range(num_cases):
        num_input = int(input())
        # num_input = 65
        # string_input = "3 30 15 15151 15153 1515152"
        # string_input = "891 885 814 442 128 180 785 538 871 562 582 166 803 733 333 855 760 848 378 463 11 820 151 378 942 837 721 300 113 760 957 391 153 49 15 45 919 151 102 296 822 732 502 246 962 58 511 929 806 174 138 670 97 504 422 676 519 301 490 263 55 264 644 890 251"
        # string_input = "598 649 705 551 151 977 413 555 798 505 382 749 66 379 700 210 130 554 484 448 608 774 323 306 177 54 225 631 367 401 445 371 286 17 899 156 134 558 577 179 267 358 712 879 615 820 738 134 592 721 763 634 198 32 589 590 874 878 305 359 201 255 961 916 948"
        string_input = input()
        splitted = string_input.split(" ")
        # sortedList = sorted(splitted[:num_input], key=functools.cmp_to_key(comparator), reverse=True)
        # print(sortedList)
        results.append(functools.reduce(lambda x, y: x+y, sortedList))
    for result in results:
        print(result)