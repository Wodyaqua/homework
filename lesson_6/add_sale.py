import sys

price = sys.argv[1]

with open('sales.csv', 'a', encoding='utf-8') as f:
    f.write(price + '\n')
