'''Functions - Assignment-3 - Using Bisection Search to Make the Program Faster'''
def payingdebt_off_in_ayear(balance, annual_interest_rate):
    """function for calculating the lowest payment"""
    def balance_func(balance, pay, annual_interest_rate):
        """A function to calculate balance"""
        balance_new = balance
        for _ in range(1, 13):
            balance_u = balance_new - pay
            balance_new = balance_u*(1 + (annual_interest_rate/12.0))
        return balance_new
    payment_low = balance/12.0
    monthly_interest_rate = annual_interest_rate/12.0
    payment_high = (balance*((1 + monthly_interest_rate)**12))/12.0
    payment = (payment_high + payment_low)/2.0
    epsilon = 0.05556
    while True:
        #print(balance_func(balance, payment, annual_interest_rate))
        if  balance_func(balance, payment, annual_interest_rate) > epsilon:
            payment_low = payment
        elif balance_func(balance, payment, annual_interest_rate) < -epsilon:
            payment_high = payment
        else:
            return round(payment, 2)
        payment = (payment_high + payment_low)/2.0
    #if balance_func(balance, payment, annual_interest_rate) <= epsilon:

def main():
    """
    A function for output
    """
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment: " + str(payingdebt_off_in_ayear(data[0], data[1])))
if __name__ == "__main__":
    main()
