"""
There is a large pile of socks that must be paired by color.
Given an array of integers representing the color of each sock, 
determine how many pairs of socks with matching colors there are.
"""


def sock_merchant(n, ar):
    count = 0

    x = set()

    for i in ar:
        if i in x:
            x.remove(i)
            count += 1
        else:
            x.add(i)
    return count


if __name__ == "__main__":
    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sock_merchant(n, ar)
