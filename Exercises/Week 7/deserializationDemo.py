import json

with open ('accounts.json', 'r') as accounts:
    #accounts_json = json.load(accounts)
    print(json.dumps(json.load(accounts), indent=4))


#print(accounts_json)