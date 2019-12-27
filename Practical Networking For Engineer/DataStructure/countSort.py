
# Function to sort the array by the Countsort algorithm
def countSort(aList: list) -> list:
    copyList = aList.copy()

    # Create list has
    output = [0 for i in range(0, len(copyList))]

    RANGE = max(copyList)

    count = [0 for i in range(0, RANGE + 1) ]
    for item in copyList:
        count[item] += 1

    for i in range(0, RANGE):
        count[i+1] += count[i]

    for item in copyList:
        output[count[item]-1] = item
        count[item] -= 1

    for i in range(0, len(copyList)):
        copyList[i] = output[i]

    return copyList


if __name__ == '__main__':
    a = [0, 0, 1, 560, 560, 790, 4, 1, 2, 0, 7, 5, 2, 52]
    print(countSort(a))
