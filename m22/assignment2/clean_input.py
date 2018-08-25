'''
Write a function to clean up a given string by removing
the special characters and retain
alphabets in both upper and lower case and numbers.
'''
import re
def clean_string(string):
    """clean sring"""
    regex = re.compile(r'[^a-z ]','0') 
    string = regex.sub('', string)
    str1 = string.replace(" ", "")
    return str1
def main():
    """main func"""
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
