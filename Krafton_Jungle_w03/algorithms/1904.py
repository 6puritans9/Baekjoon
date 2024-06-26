import sys


def get_input():
    return sys.stdin.readline().rstrip()


def get_combinations(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 15746

    return dp[n]


if __name__ == "__main__":
    n = int(get_input())
    print(get_combinations(n))
