import csv
with open('accounts.csv', 'w', newline = '') as accounts:
    wrt = csv.writer(accounts)
    wrt.writerow([100, 'Jones', 24.98])
    wrt.writerow([200, 'Doe', 345.67])
    wrt.writerow([300, 'White', 0.00])
    wrt.writerow([400, 'Stone', -42.16])
    wrt.writerow([500, 'Rich', 224.62])
    
