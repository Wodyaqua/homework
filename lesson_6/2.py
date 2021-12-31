with open('nginx_logs.txt') as f:
    data = []
    spammers = {}
    for line in f:
        line = line.split()
        data.append((line[0], line[5][1:], line[6]))
        spammers.setdefault(line[0], 0)
        spammers[line[0]] += 1

# print(data)
output = sorted(spammers.items(), key=lambda x: x[1], reverse=True)
print(output[0])
