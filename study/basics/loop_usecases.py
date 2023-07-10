# WHILE LOOPS

# While loops are used to repeat a block of code until a condition is met.
# It's also called a conditional loop or indefinite loop.

n = 5  # we need to declare counters before the loop
while n > 0:
    n -= 1
    if n == 2:
        continue  # continue skips the rest of the code in the loop and goes back to the beginning
    if n == 1:
        break  # break stops the loop
    print(n)
else:
    print('loop ended normally')  # else is executed when the loop is finished completely
print('Loop ended.')  # this is executed after the loop independetly of the loop's outcome

# one-line while loop
n = 5
while n > 0: n -= 1; print(n)

# FOR LOOPS

# For loops are used to iterate over a sequence (list, tuple, string) or other iterable objects.
# It's also called a definite loop or a counted loop.

# collection-based iteration
# iterables are objects that can be iterated over like lists, tuples, strings, dictionaries, etc.
# the for loop assigns each item of the iterable to the variable in the loop
for i in [1, 2, 3]:
    print(i)

# iterable objejcts can be used to generate iterators
iterator = iter([1, 2, 3])
print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
# print(next(iterator))  # StopIteration error

# range() function
for i in range(5):  # range() returns an iterable object
    print(i)

# iterating over dictionaries
d = {'a': 1, 'b': 2, 'c': 3}
for key, value in d.items():  # .items() returns a list of tuples
    print(key, value)  # unpacking the tuples

# break and continue work the same way as in while loops, as well as else
# else is executed when the loop is finished completely without break
