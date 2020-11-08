import argparse

def getLastStudent(numberOfStudents, treats, startingChair):
    lastStudent=startingChair
    for i in range(1,treats):
        lastStudent = lastStudent + 1
        if lastStudent > numberOfStudents:
            lastStudent=1
    return lastStudent

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-numberOfStudents', type=int)
    parser.add_argument('-treats', type=int)
    parser.add_argument('-startingChair', type=int)
    args = parser.parse_args()
    print(getLastStudent(args.numberOfStudents, args.treats, args.startingChair))