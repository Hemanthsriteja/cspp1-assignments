'''Exercise: Assignment-1'''
# This function takes in one number and returns one number.
def fact_rec(n_v):
    '''
    n is positive Integer
    returns: a positive integer, the factorial of n
    '''
    # Your code here
    if n_v <= 1:
        return 1
    return n_v*fact_rec(n_v-1)
def main():
    """def fun"""
    a_v = input()
    print(fact_rec(int(a_v)))
if __name__ == "__main__":
    main()
