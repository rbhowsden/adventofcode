with open('input.txt') as f:
    lines = f.readlines()

def yeet(x):
    x = x.strip('\n')
    half = len(x)//2
    s1 = set(x[half:])
    s2 = set(x[:half])
    item = list(s1.intersection(s2))[0]
    return (ord(item) - 38) % 58

print(sum(map(yeet, lines)))