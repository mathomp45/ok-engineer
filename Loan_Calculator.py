import math
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--type', metavar='type', help='indicates the type of payment', required=True, choices=['annuity',
                                                                                                            'diff'])
parser.add_argument("--principal", metavar='principal', type=int, help='loan principal')
parser.add_argument('--interest', metavar='interest', type=float)
parser.add_argument('--payment', metavar='payment', type=int, help='Is the monthly payment amount')
parser.add_argument('--periods', metavar='periods', type=int, help='number of months')

args = parser.parse_args()
calc_type = args.type

if calc_type == 'annuity':
    if args.interest is None:
        print("Incorrect Parameters")
    else:
        if args.principal is None:
            a = args.payment
            n = args.periods
            interest_rate = args.interest
            i = interest_rate / 100 / 12
            p = int(a / ((i * math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1)))
            overpayment = (a * n) - p
            print("Your loan principal = " + str(p) + "!")
            print(f'Overpayment =  {overpayment} ')
        elif args.payment is None:
            p = args.principal
            n = args.periods
            interest_rate = args.interest
            i = interest_rate / 100 / 12

            a = math.ceil(p * i * (math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))
            print(f'Your annuity payment ={a}!')
            total_payment = a * n
            overpayment = total_payment - p
            print(f'Overpayment = {overpayment}')

        elif args.periods is None:
            p = args.principal
            a = args.payment
            interest_rate = args.interest
            i = interest_rate / 100 / 12
            n = math.ceil(math.log((a / (a - i * p)), 1 + i))
            Total_payment = a * n
            Overpayment = Total_payment - p
            if n < 12:
                print(f'It will take {n} months to repay this loan!')
                print(f'Overpayment = {Overpayment}')
            elif n == 12:
                print(f'It will take 1 year to repay this loan!')
                print(f'Overpayment = {Overpayment}')
            else:
                y = n // 12
                r = n % 12
                if r != 1:
                    print(f'it will take {y} years and {r} months to repay this loan!')
                    print(f'Overpayment = {Overpayment}')
                else:
                    print(f'it will take {y} years and {r} month to repay this loan!')
                    print(f'Overpayment = {Overpayment}')

elif calc_type == "diff":
    if args.interest is None:
        print("Incorrect Parameters")
    else:
        p = args.principal
        n = args.periods
        interest_rate = args.interest
        i = float(interest_rate / 100 / 12)
        m = n
        a = math.ceil(p * i * (math.pow(1 + i, n)) / (math.pow(1 + i, n) - 1))
        Total_payment = 0

        for m in range(1, n + 1):
            dm = (p / n) + i * (p - (p * (m - 1)) / n)
            print(f'Month {m} : payment is {math.ceil(dm)}')
            Total_payment += math.ceil(dm)
        Overpayment = Total_payment - p
        print(f'with overpayment = {math.floor(Overpayment)}')
elif calc_type != "annuity" or "diff":
    print('Incorrect parameters')
