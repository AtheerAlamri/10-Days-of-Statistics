# Complete the 'Mean, Median and Mode' function below.

import statistics
from scipy import stats


# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
def calculate(arr: list):
    print(round(float(statistics.mean(arr)), 1))
    print(round(float(statistics.median(arr)), 1))
    print(int(stats.mode(arr)[0]))


if __name__ == '__main__':
    X = list(map(int, input().split()))

    calculate(X)
