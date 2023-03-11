# Written by *** for COMP9021

# Prompts the user for a positive integer.
# - When written in base 3, its consecutive digits read
#   from left to right represent the directions to take, with
#   * 0 meaning going South,
#   * 1 meaning South West,
#   * 2 meaning South East.
#
# Prints out:
# - the representation of the second digit in base 3;
# - the corresponding sequence of directions to take, as arrows;
# - the sequence of arrows again, but nicely displayed.
#
# The leftmost arrow is printed out with no space to the left.
#
# The arrows are the Unicode characters of code point
# 0x21e9 and 0x2b02 and 0x2b03.

import sys

try:
    encoded_directions = int(input('Enter a positive integer: '))
    if encoded_directions < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()


#INSERT YOUR CODE HERE
def to_base_3(num):
    if num == 0:
        return "0"
    digits = []
    while num > 0:
        num, remainder = divmod(num, 3)
        digits.append(str(remainder))
    return "".join(digits[::-1])

arrow_south = chr(0x21e9)
arrow_south_east = chr(0x2b02)
arrow_south_west = chr(0x2b03)

directions = to_base_3(encoded_directions)
print("In base 3, the input reads as: ", end = "")
print(directions)
print()
print("So that's how you want to go: ", end = "")
for e in directions:
    if e == "0":
        print(arrow_south, end = "")
    elif e == "1":
        print(arrow_south_west, end="")
    else:
        print(arrow_south_east, end ="")
print("\n")

print("Let's go then!")




# Initialize variables to track the current position of the arrow
ones = directions.count('1')
twos = directions.count('2')
indentation = ones + twos
min_idnet = indentation

for d in directions:
    if d == '1':
        indentation -= 1
        min_idnet = min(indentation, ones+twos)
    elif d == '2':
        indentation += 1

if min_idnet != 0:
    indentation = ones + twos - min_idnet
else:
    indentation = ones + twos

# Loop over the directions and print the arrows
for i, direction in enumerate(directions):
    if direction == '0':
        print(' ' * indentation + arrow_south)
    elif direction == '1':
        print(' ' * indentation + arrow_south_west)
        indentation -= 1

    elif direction == '2':
        print(' ' * indentation + arrow_south_east)
        indentation += 1




