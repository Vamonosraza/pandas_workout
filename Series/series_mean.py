import pandas as pd
import numpy as np

g = np.random.default_rng(0)
months = 'Sep Oct Nov Dec Jan Feb Mar Apr May Jun'.split()
s = pd.Series(g.integers(10, 100, 10), index=months)

print(f'Yealry average: {s.mean()}')

first_half = s['Sep':'Jan'].mean()
second_half = s['Feb':'Jun'].mean()

print(f'First half average: {first_half}')
print(f'Second half average: {second_half}')

print(f'Improvement: {second_half - first_half}')

highest_score = s.max()
highest_month_score = s.idxmax()

print(f'Highest score: {highest_score} in {highest_month_score}')

print('This will describe the series. It does this to show the mean, std, min, max, etc.')
print(s.describe())

# A series is a dictionary, so we can sort it by index
print('This will show the series sorted by index')
print(s)
