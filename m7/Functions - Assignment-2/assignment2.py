'''Assignment-2 - Paying Debt off in a Year'''
def paying_debtoffinayear(balance, annual_interest_rate):
    """defining function"""
    balance_new = balance
    payment_balance = 0
    while True:
        i = 12
        balance_new = balance
        while i != 0:
            unpaid_balance = balance_new - payment_balance
            balance_new = unpaid_balance + ((annual_interest_rate / 12.0) * unpaid_balance)
            i -= 1
        if balance_new > 0:
            payment_balance += 10
        else:
            break
    return payment_balance
def main():
    """Defining main"""
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment: " + str(paying_debtoffinayear(data[0], data[1])))
if __name__ == "__main__":
    main()
