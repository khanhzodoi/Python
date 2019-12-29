# Function to sort the array by the Countsort algorithm
def countSort(aList: list) -> list:
    # Create list has the same length as the copyList
    output = [0 for i in range(0, len(aList))]

    # Find the max vaulue in the list to be the range for count
    RANGE = max(aList)

    # Create count to save the store the number of values in copyList
    count = [0 for i in range(0, RANGE + 1)]

    # Store count of each character
    for item in aList:
        count[item] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(0, RANGE):
        count[i+1] += count[i]

    for item in aList:
        output[count[item]-1] = item
        count[item] -= 1

    return output


if __name__ == '__main__':
    a = [0, 0, 1, 560, 560, 790, 4, 1, 2, 0, 7, 5, 2, 52]
    print(countSort(a))
