'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def mult_line(input_v):

list_1 = input_v
    list_1 = list_1.split("\n")
    return list_1
    # i = 2
    # for set_list in list_1:
    #     if " follows " in set_list:
    #         list_i = set_list
    #         i += 1
    #         if list_i != '':
    #             list_i = list_i.split(' follows ')
    #             #print(list_i)
    #             NETDICT[list_i[0]] = list_i[1].split(',')
    # return NETDICT


def main():
    '''
        handling testcase input and printing output
    '''
    store_string = ''
    num_lines = int(input())
    for i in range(num_lines):
        i += 1
        store_string += input()
        store_string += '\n'
    print(mult_line(store_string))


if __name__ == '__main__':
    main()
