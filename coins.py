def coins():

    input('Enter the amount of money to convert')


# Asks for the total number of dollars
Dollars = int(input('# of dollars: '))
# Asks for the number cents
Cents = int(input('# of cents: '))

# Displays the total number of cents for the total number of dollars
Dollars1 = int(Dollars*100)
# Displays the  total number of cents
Total = int(Dollars1+Cents)

# Q is the total num of quarters for the dollars entered
Q = int(Dollars*4)
# Q1 is the total num of quarters for the cents entered
Q1 = int(Cents/25)
# Q2 is the total num of quarters
Q2 = int(Q+Q1)
# QC is the cents value for the total num of quarters
QC = int(25*Q2)

# D is the total num of dimes left over
D = int((Total-QC)/10)
# DC is the cents value for the dimes left over
DC = int(D*10)
# D2 is the cents left over
D1 = int(Total-(QC+DC))

# N is the total number of nickels left over
N = int(D1/5)
# N is the cents value for the nickels left over
NC = int(N*5)
# N1 is the cents left over
N1 = (Total-(DC+QC))

# P is the pennies left over
P = int(N1-NC)


print('The coins are', Q2, 'quarters,', D, 'dimes,', N, 'nickels and', P, 'pennies')

