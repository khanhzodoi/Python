

def collartz(number):
    if number % 2 == 0:
        return number // 2
    else:
        a = 3 * number + 1
        print(a)
        return a

if __name__ == "__main__":
    while True:
        try:
            num = int(input("Type an integer number: "))
            break
        except ValueError:
            print("The value is not an integer number!!!")
    while True:
        num = collartz(num)
        if num == 1:
            print(num)
            break
    
