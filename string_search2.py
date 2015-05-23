# string_search2.py
#finds all occurrences of a string in a text file, counts them, and prints them out.

import re

def main():
    fname = open("placeholder.txt", "r")
    regex = re.compile(r'lor', re.IGNORECASE)
    count = 0
    for line in fname:
        string_search = regex.findall(line)
        for word in string_search:
            count +=1
            print(count, word)

if __name__ == '__main__': main()