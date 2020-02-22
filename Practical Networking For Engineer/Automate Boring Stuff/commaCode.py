import copy
def func(l: list):
    s = ""
    new_list = copy.deepcopy(l)
    new_list.insert(-1, "and")
    for item in new_list:
        if item != "and" and item != new_list[-1]:
            s = s + str(item) + ", "
        else:
            s = s + str(item) + " "

    
    return s



spam = ['apples', 'bananas', 'tofu', 'cats', 'fuck', ['now', 1]]
print(func(spam))
