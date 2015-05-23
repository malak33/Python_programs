# string_search3.py
#finds all occurrences of a string in a text file, counts them, and prints them out.

import re

def main():
    #enter the file name
    fname = input("Enter filename: ")
    #change file name to variable to use
    #ask for search regex
    string = input("Enter the string/regex you would like to search for: ")

    infile = open(fname,"r")
    #create regex to search for string
    regex = re.compile(string, re.IGNORECASE)
    count = 0
    #the algorithm,
    for i in infile:
        string_search = regex.findall(i)
        for word in string_search:
            count +=1
            print("{0:4} {1:6}".format(count, word))

if __name__ == '__main__': main()