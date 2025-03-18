def max_hamster(S: int, C: int, hamster: list[list[int]]) -> int:
    """
    :param S: Food for hamster per day
    :param C: Quantity hamster
    :param hamster: Appetite and greed
    :return: Number of hamsters that can live together
    """

    sorted_hamster = sorted(hamster, key=lambda x: x[1])
    result = 0

    for i in range(C):
        leftover_food = S
        result += 1
        for j in range(i+1):
            leftover_food -= sorted_hamster[j][0] + sorted_hamster[j][1] * i

        if leftover_food < 0:
            return result - 1

    return result
