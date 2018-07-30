# cracks passwords

# salt is first 2 characters of argv
from sys import argv
from crypt import crypt
# command lines arguments are array at argv
# remember that argv[0] is the program name

# all chars rated by frequency of use in oxford dictionary, not including space
myDict = "eEtTaAoOiInNsSrRhHlLdDcCuUmMfFpPgGwWyYbBvVkKxXjJqQzZ"
salt = ""
myArgument = ""


def main():
    if len(argv) == 2 and len(argv[1]) == 13:
        # there is one command line argument
        # and it has a length of 13
        myArgument = argv[1]
        # assign salt to first 2 chars of hash
        salt = myArgument[0:2]
        print(myFunction(salt, myArgument))

    else:
        # orelse remind of proper usage
        print("Usage: python crack.py <hashed password>")
    return


def myFunction(salt, myArgument):
    for c in myDict:
        if crypt(c, salt) == myArgument:
            return c
    for c in myDict:
        for a in myDict:
            if crypt(c + a, salt) == myArgument:
                return c + a
    for c in myDict:
        for a in myDict:
            for r in myDict:
                if crypt(c + a + r, salt) == myArgument:
                    return c + a + r
    for c in myDict:
        for a in myDict:
            for r in myDict:
                for e in myDict:
                    if crypt(c + a + r + e, salt) == myArgument:
                        return c + a + r + e
    for c in myDict:
        for a in myDict:
            for r in myDict:
                for e in myDict:
                    for s in myDict:
                        if crypt(c + a + r + e + s, salt) == myArgument:
                            return c + a + r + e + s
    return "Failed to find password"


if __name__ == "__main__":
    main()