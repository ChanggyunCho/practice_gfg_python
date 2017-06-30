# http://practice.geeksforgeeks.org/problems/a-simple-fraction/0

def calculate(M, N):
    """calculate M / N"""
    integer = M // N
    remainder = M % N

    ret = str(integer)

    if remainder > 0:
        ret += "."
        intermediate = [(integer, remainder)]
        repeatFrom  = -1
        while remainder > 0:
            remainder *= 10
            integer = remainder // N
            remainder = remainder % N
            if remainder != 0:
                # check pattern,
                samePattern = next(((idx, item) for idx, item in enumerate(intermediate) if item[1] == remainder), None)
                intermediate.append((integer, remainder))

                if samePattern is not None:
                    # print(samePattern)
                    repeatFrom = samePattern[0]+1
                    break
            else:
                intermediate.append((integer, remainder))
        print(intermediate, repeatFrom)
        
        if repeatFrom >= 0:
            for i in range(1, repeatFrom):
                ret += str(intermediate[i][0])
            ret += "("
            for i in range(repeatFrom, len(intermediate)):
                ret += str(intermediate[i][0])
            ret += ")"
        else:
            for (n, r) in intermediate[1:]:
                ret += str(n)
    return ret
    
if __name__ == "__main__":
    num_cases = int(input())
    results = []
    for _ in range(num_cases):
        # M = int("5928")
        M = int(input())
        # N = int("9900")
        N = int(input())
        results.append(calculate(M, N))
    for result in results:
        print(result)