with open('input.txt') as f:
    lines = f.readlines()

outcomes = {
    'A X\n': 0 + 3,
    'A Y\n': 3 + 1,
    'A Z\n': 6 + 2,
    'B X\n': 0 + 1,
    'B Y\n': 3 + 2,
    'B Z\n': 6 + 3,
    'C X\n': 0 + 2,
    'C Y\n': 3 + 3,
    'C Z\n': 6 + 1,
}

sum(list(map(outcomes.get, lines)))

