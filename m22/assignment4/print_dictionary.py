'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Format of the printing should be one key per line and separate
the key and frequency with a SPACE - SPACE.
'''

def print_dictionary(d):
    keys = sorted(d.keys())
    for key in keys:
        print(key, "-", d[key])

def main():
    d = eval(input())
    print_dictionary(d)

if __name__ == '__main__':
    main()
