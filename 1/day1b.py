with open('input.txt') as f:
    lines = f.readlines()

counter = 0
calories = []

for x in lines:
    if x == '\n':
        calories.append(counter)
        counter = 0
        continue
    else:
        counter += int(x)

calories.sort()

print(sum(calories[-3:]))