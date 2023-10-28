string = input("Enter a string to be reversed: ")

"""
Goal: Print the string and the reversed string, preferably using a loop.
Examples: 
    Input     ->   Output
    ----------------------
    "hello"   ->   "helloolleh"
    "racecar" ->   "racecarracecar"
    "a"       ->   "aa"
    ""        ->   ""
"""

# Your code here
for i in range(len(string)-1, -1, -1):
    print(string[i])