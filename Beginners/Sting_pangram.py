# Write a Python function to check whether a string is pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

myPharse = "The quick brown fox jumps over the lazy dog"

def pangram(pharse):
    alphabet =  "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in pharse:
            print(False)
    print(True)


if __name__ == '__main__':
    pangram(myPharse)