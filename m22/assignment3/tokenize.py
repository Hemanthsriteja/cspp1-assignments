'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''

def tokenize(string1):
    freq = {}
    for i_i in string1:
        freq[i_i] = freq.get(i_i, 0) + 1
    return freq
            
def main():
    string = input()
    for _ in range(int(string)):
        data = input()
        string1 = data.split()
    tokenize(string1)

#     a_v = {}
#     for j in word_v:
#         if j in hand_v:
#             a_v[j] = hand_v[j]-1
#     return a_v
# def main():
#     '''main'''
#     n_v = input()
#     a_dict = {}
#     for _ in range(int(n_v)):
#         data = input()
#         l_v = data.split()
#         a_dict[l_v[0]] = int(l_v[1])
#     data1_v = input()
#     print(update_hand(a_dict, data1_v))
    

if __name__ == '__main__':
    main()
