# Complete the 'interQuartile' function below.

def find_median(arr: list) -> int:
    if len(arr) % 2 == 1:
        return arr[len(arr) // 2]
    else:
        return (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) // 2


# The function accepts following parameters:
#  1. INTEGER length_values Array
#  2. INTEGER_ARRAY values
#  3. INTEGER_ARRAY freqs
def inter_quartile(length_values: int, values: list, freqs: list) -> float:
    interQuartile_arr = []
    for i in range(length_values):
        for j in range(freqs[i]):
            interQuartile_arr.append(values[i])
    interQuartile_arr.sort()

    #  IQR = Q3 −  Q1
    q1 = find_median(interQuartile_arr[:len(interQuartile_arr) // 2])
    q3 = find_median(interQuartile_arr[len(interQuartile_arr) // 2 + len(interQuartile_arr) % 2:])

    IQR = q3 - q1
    return round(float(IQR), 1)


if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    print(inter_quartile(n, val, freq))

