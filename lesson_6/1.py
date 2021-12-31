with open('nginx_logs.txt') as f:
    data = []
    for line in f:
        line = line.split()
        data.append((line[0], line[5][1:], line[6]))

print(data)
