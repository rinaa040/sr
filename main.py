import csv
import json

lst = []
with open('users.csv', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    for row in reader:
        if len(row["password"]) >= 8 and len(set(row['first_name']) & (set(row["password"]) | set(row['last_name']))) / (
                len(row['first_name']) + len(row['last_name']) + len(row["password"])) <= 0.5:
            del row['id'], row['password']
            lst.append(row)

with open('cats_3.json', 'w') as cat_file:
    json.dump(lst, cat_file)

