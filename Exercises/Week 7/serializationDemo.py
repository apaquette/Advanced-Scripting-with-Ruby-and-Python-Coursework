import json

accounts_dict = {'accounts':[
    {'account': 100, 'name': 'Jones', 'balance':24.98},
    {'account': 200, 'name': 'Doe', 'balance':345.67}]}

# serializing object to JSON
with open('accounts.json', 'w') as accounts:
    json.dump(accounts_dict, accounts)