# http://practice.geeksforgeeks.org/problems/n-queen-problem/0

def nqueen_recur(n, depth, location, results):
    for i in range(1, n+1):
        # check attackable queen
        find_queen = False
        for j in range(0, depth):
            if (location[j] == (i-(depth-j)) or location[j] == (i+(depth-j)) or (location[j] == i)):
                # find queen
                find_queen = True
                break
        if not find_queen:
            sub_location = list(location)
            sub_location.append(i)
            if n == depth + 1:
                results.append(sub_location)
            else:
                nqueen_recur(n, depth+1, sub_location, results)

def nqueen(n):
    result = []
    nqueen_recur(n, 0, [], result)
    return result


if __name__ == "__main__":
    no_cases = int(input())
    results = []
    for _ in range(no_cases):
        n = int(input())
        results.append(nqueen(n))

    # print result
    for result in results:
        if len(result) == 0:
            print("-1")
        else:
            string = ""
            for ans in result:
                string += "["
                for elem in ans:
                    string += (str(elem) + " ")
                string += "] "
            print(string)
