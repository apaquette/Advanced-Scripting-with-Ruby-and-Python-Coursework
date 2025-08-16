import csv

with open('accounts.csv', 'r', newline='') as accounts:
    print(f'{"Account":<10}{"Name":<10}{"Balance":>10}')
    read = csv.reader(accounts)
    for record in read:
        account, name, balance = record
        print(f'{account:<10}{name:<10}{balance:>10}')

import pandas as pd

df = pd.read_csv("accounts.csv", names=['account', 'name', 'balance'])
print(df)

#saving DataFrame to CSV file
df.to_csv('accountDF.csv', index=False)