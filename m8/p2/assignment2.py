''' sumofdigits, that takes in one number and returns the sum of digits of given number'''
def sum_of_digits(n_v):
    '''
    n is positive Integer
    returns: a positive integer, the sum of digits of n.
    '''
    # Your code here
    if n_v == 0:
        return 0
    return n_v%10 + sum_of_digits(n_v//10)
def main():
    """def func"""
    a_v = input()
    print(sum_of_digits(int(a_v)))
if __name__ == "__main__":
    main()
