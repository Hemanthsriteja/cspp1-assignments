'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(a_dict):
    """token"""
    for i_i in a_dict:
        a_dict[i_i] = a_dict.get(i_i, 0) + 1
    print(a_dict)
def main():
    '''main'''
    n_v = input()
    a_dict = {}
    for _ in range(int(n_v)):
        data = input()
        l_v = data.split()
        a_dict[l_v[0]] = int(l_v[1])
    tokenize(a_dict)
if __name__ == "__main__":
    main()
