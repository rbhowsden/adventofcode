with open('input.txt') as f:
    lines = f.readlines()

lines = list(map(lambda x: x.strip('\n'), lines))
groups = list(zip(*(iter(lines),) *3))

def yeet(x):
    s1 = set(x[0])
    s2 = set(x[1])
    s3 = set(x[2])
    item = list(s1.intersection(s2).intersection(s3))[0]
    return (ord(item) - 38) % 58

print(sum(map(yeet, groups)))