'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    keys = sorted(string.keys())
    for key in keys:
        print(key, " - ", string[key])

def main():
    pass

if __name__ == '__main__':
    main()
