# Complete the 'quartiles' function below.

# The function is expected to return the Median is in either half of the array
def find_median(arr):
    if len(arr) % 2 == 1:
        return arr[len(arr) // 2]
    else:
        return (arr[len(arr) // 2] + arr[len(arr) // 2 - 1]) // 2


# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
def quartiles(arr):
    q1 = find_median(arr[:len(arr) // 2])
    q2 = find_median(arr)
    q3 = find_median(arr[len(arr) // 2 + len(arr) % 2:])

    return q1, q2, q3


if __name__ == '__main__':
    fptr = open('Output.txt', 'w')

    n = int(input().strip())

    data = sorted(list(map(int, input().rstrip().split())))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
