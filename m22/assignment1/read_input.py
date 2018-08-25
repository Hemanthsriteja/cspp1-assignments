'''
Write a python program to read multiple lines of text input and store the input into a string.
'''
def mult_line(input_v):
    """mult_line"""
    list_1 = input_v
    return list_1
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
