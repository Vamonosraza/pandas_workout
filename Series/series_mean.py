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
