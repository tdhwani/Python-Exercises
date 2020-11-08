import argparse

def peopleWatch(heightOfPeople):
    answer = []
    for i in range(0,len(heightOfPeople)-1):
        curr = i
        tallest = i
        for j in range(i+1,len(heightOfPeople)):
            if heightOfPeople[j] > heightOfPeople[tallest]:
                tallest = j
                break
        if heightOfPeople[tallest] != heightOfPeople[curr]:
            answer.append(tallest)
        else:
            answer.append(None)
    answer.append(None)
    return answer

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-heightOfPeople', nargs='+')
    args = parser.parse_args()
    print(peopleWatch(args.heightOfPeople))