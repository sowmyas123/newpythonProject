import csv

test_data = [
    ['Name', 'Age', 'City'],
    ['sowmya', 20, 'Bangalore'],
    ['siri', 1, 'Mandya']
]

try:
    with open('mydata.csv', 'w') as file:
        writer = csv.writer(file)
        for row in test_data:
            writer.writerow(row)
except FileNotFoundError as f:
    print(f)
finally:
    print("close your files")
