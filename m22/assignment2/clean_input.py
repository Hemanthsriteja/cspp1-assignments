'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''
import re

def clean_string(string):
    regex = re.compile('[^a-z ]')
    

    string = regex.sub('', string)
    return string
    list_ofwords = string.split('').strip()
    for index in range(len(list_ofwords)):
        list_ofwords[index] = list_ofwords[index].strip()
    # print(list_ofwords)
    return list_ofwords

def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
