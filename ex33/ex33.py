
def make_sequence_of_numbers(low, high):
    """ Make a list with low and high interval."""
    # create an empty list
    numbers = []
    # if low is still less than high, while-loop keeps repeating
    for i in range(low, high, 2):
        # add value i to the bottom of the list
        numbers.append(i)
    # return the appended list
    return numbers

def print_list(numbers):
    """Print out the input list"""

    count = 0
    for num in numbers:
        print(f"numbers ({count}): {num}")
        count += 1



def main():
    print("Enter the numbers a and b for which the list contains the values between." )
    low = int(input("> Enter the low number (a): "))
    high = int(input("> Enter the high number (b): "))
    numbers = make_sequence_of_numbers(low, high)
    print_list(numbers)

main()
