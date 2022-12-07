from collections import Counter

with open('input.txt') as f:
    line = f.readlines()[0]

ss_len = 14
init_count = Counter(line[0:ss_len])

for x in range(ss_len, len(line)):
    if len(init_count) == ss_len:
        print(f'Answer is {x}')
        break

    init_count.update(line[x])
    init_count.subtract(line[x-ss_len])

    if init_count[line[x-ss_len]] == 0:
        del init_count[line[x-ss_len]]