import argparse

def checkFactorial(n):
    i = 1
    while (True):
        if (n % i == 0):
            n = n/i
        else:
            break
        i = i+1
    if (n == 1):
        return True
    else:
        return False

def leastFactorial(num):
    for i in range(num, 121):
        if checkFactorial(i):
            return i
    return i

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-number', type=int)
    args = parser.parse_args()
    print(leastFactorial(args.number))