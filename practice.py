string = input("Enter a string to be reversed: ")

"""
Goal: Print the reversed string, preferably using a loop.
Examples: 
    Input     ->   Output
    ----------------------
    "hello"   ->   "olleh"
    "racecar" ->   "racecar"
    "a"       ->   "a"
    ""        ->   ""
"""

# Your code here
for i in range (len(string)-1, -1, -1):
    print(string[i])