# Exercise: Assignment-1
# This function takes in one number and returns one number.
def fact_rec(n):
    '''
    n is positive Integer
    returns: a positive integer, the factorial of n
    '''
    # Your code here
    if n <= 1:
        return 1
    else:
        return n*fact_rec(n-1)
    


def main():
    a = input()
    print(fact_rec(int(a)))    

if __name__ == "__main__":
    main()
