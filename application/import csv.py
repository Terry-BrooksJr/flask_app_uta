import csv

with open('/users.csv', 'w', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
