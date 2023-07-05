# int
num_int = 10
# float
num_float = 10.5
# complex
num_complex = 3.14j

# we don't use complex very often, so let's focus on int and float
# float is useful but not super accurate when rounding up numbers
# int is useful for counting things, but not for calculating things

# decimal
num_dec = 10.99
# fraction
num_frac = 1/3

# decimal and fraction are not built-in, we need to import them
from decimal import Decimal
from fractions import Fraction

num_dec = Decimal('10.99')
num_frac = Fraction(1, 3)

# decimal and fractions are accurate, mainly when calculating money
# but they are not as fast as float and int

print(num_dec, num_frac)

# NaN (not a number) is not equals to anythinbg, not even itself
print(float('nan') == float('nan'))  # False

# infinity is a number, but it's not equals to itself
infinite = float('inf')

# format float numbers
print(format(0.2, '.3f'))
price = 1999.99
print(f'It is: ${price:,.2f}')  # $1,999.99
ratio = 0.5
print(f'This code has {ratio:.1%} coverage')  # 50.0%


# Functions
print(round(0.2))
print(round(2.31, 1))  # round to 1 decimal place

print(abs(-2.31))  # absolute value, positive number

x = 0.75
y = 2.0
print(x.is_integer(), y.is_integer())  # check if float is integer
print(x.as_integer_ratio())