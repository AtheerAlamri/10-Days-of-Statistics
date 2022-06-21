# Complete the 'weightedMean' function below.

# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER_ARRAY w

def weighted_mean(x: list, w: list) -> int:
    array = []
    for num1, num2 in zip(x, w):
        array.append(num1 * num2)
    summation_array = sum(array)
    sum_weight = sum(w)

    print(round(float(summation_array / sum_weight), 1))


if __name__ == '__main__':
    n = int(input().strip())

    vals = list(map(int, input().rstrip().split()))

    weights = list(map(int, input().rstrip().split()))

    weighted_mean(vals, weights)
