'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(dict_v):
    """print dict"""
    keys = sorted(dict_v.keys())
    for key in keys:
        print(key, "-", dict_v[key])

def main():
    """main func"""
    dict_v = str(input())
    print_dictionary(dict_v)

if __name__ == '__main__':
    main()
