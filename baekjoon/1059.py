import sys

# Baekjoon 1059 - 좋은 구간
# Input:
#   L
#   sorted set S (space-separated)
#   n
# Output: number of good intervals containing n

def main() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(map(int, data))
    L = next(it)
    S = [next(it) for _ in range(L)]
    n = next(it)

    S.sort()

    # If n is already in S, no good interval can contain n without containing S.
    if n in S:
        print(0)
        return

    # Find closest lower (l) and higher (r) bounds from S around n
    l = 0  # if no element less than n, treat lower bound as 0
    r = None

    for x in S:
        if x < n:
            l = x
        elif x > n:
            r = x
            break

    # If there is no higher bound, there are no finite good intervals under the problem constraints
    if r is None:
        print(0)
        return

    # Count pairs (a, b) with l < a <= n <= b < r and a < b
    left_choices = n - l        # a in [l+1 .. n]
    right_choices = r - n       # b in [n .. r-1]
    # Exclude the single invalid pair (a = n, b = n) where a == b
    result = left_choices * right_choices - 1
    print(result)


if __name__ == "__main__":
    main()

