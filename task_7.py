import random
from prettytable import PrettyTable

N = 10000

stats_results = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78,
}


def roll_dices():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1 + dice2


def monte_carlo_simulation():
    results = {i: 0 for i in range(2, 13)}

    for _ in range(N):
        results[roll_dices()] += 1

    return {key: (value / N * 100) for key, value in results.items()}


monte_carlo_results = monte_carlo_simulation()

table = PrettyTable()

table.field_names = ["Сума", "Статистичні дані", "Монте Карло", "Похибка"]
for key, value in monte_carlo_results.items():
    table.add_row(
        [
            key,
            stats_results[key],
            round(value, 2),
            round(abs(stats_results[key] - value), 2),
        ]
    )

print(f"Результати моделювання Монте-Карло (для n={N} симуляцій):")
print(table)
