import math


def amount_of_wire(w: int, heights: list) -> float:
    """
    Calculating the largest amount of wire that will be needed to bring the electricity grid to the village
    :param w: distance between electric poles
    :param heights: an array with maximum heights
    :return: the largest amount of wire that will be needed to bring the electricity grid to the village
    """
    n = len(heights)

    dp = [{} for _ in range(n)]

    for h in range(1, heights[0] + 1):
        dp[0][h] = 0

    for i in range(1, n):
        for h in range(1, heights[i] + 1):
            max_length = 0
            for prev_h in dp[i - 1]:
                length = dp[i - 1][prev_h] + math.sqrt(w ** 2 + (h - prev_h) ** 2)
                max_length = max(max_length, length)
            dp[i][h] = max_length

    return round(max(dp[n - 1].values()), 2)


if __name__ == "__main__":
    w = 2
    heights = [3, 3, 3]
    print(amount_of_wire(w, heights))
