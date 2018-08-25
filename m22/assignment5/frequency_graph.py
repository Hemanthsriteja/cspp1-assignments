'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dict_v):
    keys = sorted(dict_v.keys())
    for key in keys:
        print(key, "-", dict_v[key]*'#')

def main():
    dict_v = eval(input())
    frequency_graph(dict_v)

if __name__ == '__main__':
    main()
