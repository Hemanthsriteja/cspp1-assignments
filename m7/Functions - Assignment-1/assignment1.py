'''Functions | Assignment-1 - Paying Debt off in a Year'''
def paying_debt_off_in_year(balance, annual_interest_rates, monthly_pay_rates):
    '''paying debt'''
    i = 1
    while i <= 12:
        montly_interest_rates = annual_interest_rates / 12.0
        min_monthly_payments = monthly_pay_rates * balance
        monthly_balances = balance - min_monthly_payments
        updated_balance = monthly_balances + (montly_interest_rates * monthly_balances)
        balance = updated_balance
        i += 1
        updated_balance_each_month = round(updated_balance, 2)
    return updated_balance_each_month
def main():
    '''main function'''
    data = input()
    data = data.split(' ')
    data = list(map(float, data))
    print("Remaining balance: " + str(paying_debt_off_in_year(data[0], data[1], data[2])))
if __name__ == "__main__":
    main()
