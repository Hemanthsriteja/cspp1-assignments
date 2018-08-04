'''Given a  number int_input, find the product of all the digits'''
def main():
    """product_of_digits"""
    n_v = int(input())
    prod_v = 1
    while n_v <= 0:
        prod_v = (prod_v) * (n_v%10)
        n_v = n_v//10
    print(prod_v)



if __name__ == "__main__":
    main()
