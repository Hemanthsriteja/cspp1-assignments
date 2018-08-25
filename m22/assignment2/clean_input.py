'''
Write a function to clean up a given string by removing
the special characters and retain
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
    """clean sring"""
    regex = re.compile(r'[^a-z ]')
    rgx1 = regex.compile(r'[0,1,2,3,4,5,6,7,8,9]')
    string = rgx1.sub('', string)
    str1 = string.replace(" ", "")
    return str1
def main():
    """main func"""
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
