# concatenation
magic_string = 'abra' + 'kadabra'
print(magic_string)
# indexing
print(magic_string[0])
print(magic_string[-1])  # last character
# slicing
print(magic_string[0:4])  # last index not included
print(magic_string[0:])  # till the end
print(magic_string[0:4:3])  # step

# string methods
print(len(magic_string))
print(magic_string.count('a'))

print(magic_string.upper())
print(magic_string.lower())
print(magic_string.capitalize())  # capitalize first letter
print(magic_string.title())  # capitalize each word

print(magic_string.find('a'))  # first occurrence, return -1 if not found
print(magic_string.rfind('a'))  # last occurrence
print(magic_string.index('a'))  # first occurrence
print(magic_string.rindex('a'))  # last occurrence
print(magic_string.startswith('a')) # returns boolean
print(magic_string.endswith('a')) # returns boolean

print(magic_string.strip())  # remove whitespace on the beginning and end
print(magic_string.lstrip())  # remove whitespace from left
print(magic_string.rstrip())  # remove whitespace from right

print(magic_string.replace('a', 'o'))
print(magic_string.split('a'))  # returns a list
print(magic_string.split('a', 1))  # returns a list with max 1 split
print(magic_string.splitlines())  # returns a list of lines

# string formatting
print(f'The magic word is: {magic_string}')
print('The magic word is: {}'.format(magic_string))

# typing strings into variables
test = '\
aaaaaaaaaaa\
bbbbbbbbbbb\
ccccccccccc'
# this is one single line string
print(test)

test2 = '''
aaaaaaaaaaa
bbbbbbbbbbb
ccccccccccc
'''.strip()
# this is a multi line string
print(test2)