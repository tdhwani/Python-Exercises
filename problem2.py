import argparse

def getTotalNumberOfLipsticks(numberOfLipsticks, numberOfLeftoversNeeded):
    total= numberOfLipsticks
    lipsticksLeft = numberOfLipsticks/numberOfLeftoversNeeded
    while (lipsticksLeft>=1):
        total = total + 1
        lipsticksLeft = lipsticksLeft - 1
        lipsticksLeft = lipsticksLeft + (1/numberOfLeftoversNeeded)
    return total

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-numberOfLipsticks', type=int)
    parser.add_argument('-numberOfLeftoversNeeded', type=int)
    args = parser.parse_args()
    print(getTotalNumberOfLipsticks(args.numberOfLipsticks, args.numberOfLeftoversNeeded))