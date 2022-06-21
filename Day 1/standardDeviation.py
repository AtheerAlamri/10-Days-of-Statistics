# Complete the 'stdDev' function below.
import math


# The function accepts INTEGER_ARRAY arr as parameter and INTEGER of array length .
def stdDev(length: int, arr: list) -> float:
    sum_ = 0
    for i in range(length):
        sum_ += (arr[i] - (sum(arr) / length)) ** 2

    standard_Dev = sum_ / length

    return round(float(math.sqrt(standard_Dev)), 1)


if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    print(stdDev(n, vals))
