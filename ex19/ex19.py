# define a function cheese_and_crackers to show the amount of cheese and the amount of crackers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheese!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


print("We can just use variables from numbers directly:")
# call cheese_and_crackers by giving two numbers as its arguments
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
# initialize two variables
amount_of_cheese = 10
amount_of_crackers = 50

# call cheese_and_crackers by giving two above variables as its arguments
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print("We can even do math inside too:")
# call cheese_and_crackers taking numbers and doing math as its arguments
cheese_and_crackers(10 + 20, 5 + 6)


print("And we can combine the two, variables and math:")
# call cheese_and_crackers taking variables and doing math as its arguments
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


###################################################################################
###################################################################################
def order_stats(total_orders, total_returns):
    print(f"You have {total_orders} orders.")
    print(f"You have {total_returns} returns.")
    print(f"Your net sales are {total_orders - total_returns}")
    print("Hopefully have a good month!\n")


#Simple arguments
order_stats(4321, 1234)


# Math
order_stats(200 + 600, 300 + 10)

#variables
total_sales = 4000
returns = 100

order_stats(total_sales, returns)

# Variables and math
jim_sales = 395
joan_sales = 600
returns = 10

order_stats(jim_sales * 2 + joan_sales * 3, returns % 2)


# Assign function to variables
order_stats_variables = order_stats
order_stats_variables(80, 149)

# With a variable number of arguments *args
var_stats = (50, 42)
order_stats(*var_stats)

# Funcion to function
def func_to_func():
    val1 = 80
    val2 = 15
    order_stats(val1, val2)

func_to_func()

#Function call itself
def recursive_function(string, num):
    print(f"#{string} - {num}")
    if num < 10:
        recursive_function(string, num + 1)

recursive_function("Hello", 1)


# user input - Don't forget to specify a type of input! In this case an integer
print("how much did you sell this month?")
user_sales = int(input('>>>'))
order_stats(user_sales, returns)

# function return the results from others
def func_A(number):
    return number + 1

def func_B(number):
    return number * 6

def func_C(number):
    return (func_A(number) + func_B(number))

print(func_C(1))
