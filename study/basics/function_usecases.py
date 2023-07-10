# ENCAPSULATION
# 1. Encapsulation is the process of restricting access to methods and variables in a class
# in order to prevent direct data modification so it prevents accidental modification of data.
# 2. Encapsulation is a protective shield that prevents the data from being accessed by the
# code outside this shield.
# 3. Encapsulation is the process of hiding implementation details from the user.
# 4. Encapsulation is the process of binding together the data and the functions that
# manipulates them.
# 5. Encapsulation is a protective barrier that prevents the code and data being randomly
# accessed by other code defined outside the class. Access to the data and code is tightly
# controlled by an interface.

def increment(number):
    def inner_increment():  # inner functions are not accessible outside the function
        return number + 1
    return inner_increment()
increment(10)

# HELPER FUNCTIONS

# Functions that will be used more than once inside another function
import csv
from collections import Counter

def process_hotspots(file):
    def most_common_provider(file_obj):  # helper function
        hotspots = []
        with file_obj as csv_file:
            content = csv.DictReader(csv_file)

            for row in content:
                hotspots.append(row["Provider"])

        counter = Counter(hotspots)
        print(
            f"There are {len(hotspots)} Wi-Fi hotspots in NYC.\n"
            f"{counter.most_common(1)[0][0]} has the most with "
            f"{counter.most_common(1)[0][1]}."
        )

    # depending on the type of file, we need to open it differently
    if isinstance(file, str):
        # Got a string-based filepath
        file_obj = open(file, "r")
        most_common_provider(file_obj)
    else:
        # Got a file object
        most_common_provider(file)


# we could do something better in this case providing a private function
# for most_common_provider adding a _ before the name of the function

# CLOSURES

# Functions are first-class objects in Python, which means that we can pass them around
# as arguments to other functions. This is a powerful feature that allows us to abstract
# away and pass around functionality in our programs.

# Higher-order functions are functions that take other functions as arguments or return
# functions as their return values. In other words, we can use functions as arguments
# to other functions or return a function from another function.

# A closure is a nested function which has access to a free variable from an enclosing
# function that has finished its execution. Three characteristics of a Python closure
# are:
# 1. It is a nested function.
# 2. It has access to a free variable in outer scope.
# 3. It is returned from the enclosing function.

# Their main feature: retaining state between function calls.

def generate_power(exponent):  # closure factory function
    def power(base):  # inner function
        return base ** exponent
    return power  # return a function using the exponent passed to the factory

raise_two = generate_power(2)  # raise_two will take exponent = 2
raise_two(3)  # it means power(3) = 3 ** 2 = 9
raise_three = generate_power(3)  # raise_three will take exponent = 3
raise_three(3)  # it means power(3) = 3 ** 3 = 27

# Closure factory that will change the state of the closure
def mean():
    nums = []
    def inner_mean(num):
        nums.append(num)
        return sum(nums) / len(nums)
    return inner_mean

sample_mean = mean()
sample_mean(10)  # 10.0
sample_mean(20)  # 15.0
sample_mean(30)  # 20.0

# we can also create getters and setters using closures, which will not provide
# as many features as a class but it is an interesting technique

# DECORATORS

# Decorators are functions that take another function as an argument, add some kind of
# functionality, and then return another function. All of this without altering the
# source code of the original function that we passed in.

def add_messages(func):  # decorator factory
    def _add_messages():  # inner function
        print("This is my first decorator") # extra functionality
        func()  # call the function passed as argument
        print("Bye!")  # extra functionality
    return _add_messages

# using the new decorator
@add_messages  # shortcut for greet = add_messages(greet)
def greet():  # function to be decorated (replacing func in the decorator factory)
    print("Hello, World!")

greet()
# This is my first decorator
# Hello, World!
# Bye!

# Example of a decorator that will time the execution of a function
import time

def timer(func):
    def _timer(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"Time elapsed: {end - start}")
    return _timer

@timer
def print_numbers():
    for i in range(10):
        print(i)

print_numbers()

# Example of a decorator that will log the execution of a function
def debug(func):
    def _debug(*args, **kwargs):
        result = func(*args, **kwargs)
        print(
            f"{func.__name__}(args: {args}, kwargs: {kwargs}) -> {result}"
        )
        return result
    return _debug

@debug
def add(a, b):
    return a + b

add(5, 6)
# add(args: (5, 6), kwargs: {}) -> 11
# 11

# Creating the power example now using decorators
def generate_power(exponent):
    def power(func):
        def inner_power(*args):
            return func(*args) ** exponent
        return inner_power
    return power

@generate_power(2)
def raise_two(n):
    return n

raise_two(7)  # 49
