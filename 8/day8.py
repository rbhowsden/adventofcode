import numpy as np

with open('input.txt') as f:
    lines = [x.strip('\n') for x in f.readlines()]

trees = list(map(lambda x: list(x), lines))

trees_arr = np.array(trees).astype(int)
x_size, y_size = trees_arr.shape

down = np.maximum.accumulate(trees_arr, axis=0)
down_0 = np.concatenate((-np.ones((1, x_size), dtype=int), down), axis=0)[:-1]

up = np.maximum.accumulate(np.flip(trees_arr, axis=0), axis=0)
up_0 = np.flip(np.concatenate((-np.ones((1, x_size), dtype=int), up), axis=0)[:-1], axis=0)

left = np.maximum.accumulate(trees_arr, axis=1)
left_0 = np.concatenate((-np.ones((y_size, 1), dtype=int), left), axis=1)[:, :-1]

right = np.maximum.accumulate(np.flip(trees_arr, axis=1), axis=1)
right_0 = np.flip(np.concatenate((-np.ones((y_size, 1), dtype=int), right), axis=1)[:, :-1], axis=1)

quadracopter = [down_0, up_0, left_0, right_0]

shorties = np.array(quadracopter).min(0)

print(sum(sum(trees_arr > shorties)))