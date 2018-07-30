# prints pyramid based on user input
from cs50 import get_int

while True:
    n = get_int("Enter a positive integer of 23 or less: ")
    if n >= 0 and n <= 23:
        break
for i in range(n):
    # calculate leading spaces and hashes
    spaces = n - (i + 1)
    hashes = n - spaces

    # print leading spaces
    print(" " * spaces, end="")

    # print first set of hashes
    print("#" * hashes, end="")

    # print 2-space separator
    print(" " * 2, end="")

    # print second set of hashes
    print("#" * hashes, end="")

    # print new line
    print()