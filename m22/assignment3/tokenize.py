'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string):
    freq = {}
    for i_i in string:
        freq[i_i] = freq.get(i_i, 0) + 1
    return freq
            
def main():
    string = input()
    

if __name__ == '__main__':
    main()
