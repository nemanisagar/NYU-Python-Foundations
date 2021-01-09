def Counter():

    print("Please enter a number of coins: ")


Q = float(input('# of quarters: '))
Q1 = float(Q*25)
D = float(input('# of dimes: '))
D1 = float(D*10)
N = float(input('# of nickles: '))
N1 = float(N*5)
P = float(input('# of pennies: '))
P1 = float(P*1)

Cents = int(Q1+D1+N1+P1)

Dollars = int(Cents/100)
C1 = Cents - (Dollars * 100)

print('The total is', Dollars, 'dollars and', C1, 'cents')