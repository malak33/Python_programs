# string_search.py
#finds all occurrences of a string in a text file, counts them, and prints them out.

import re

def main():
    #enter filename here
    file = "placeholder.txt"
    search_string = "dummy"
    lines = open( file, "r").readlines()
    count = 0
    for line in lines:
        # the search will be case insensitive
        if re.search( search_string, line, re.IGNORECASE):
           # words = line.split()
            count +=1
            print(line)

if __name__ == '__main__': main()