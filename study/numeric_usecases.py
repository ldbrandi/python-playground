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