items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}


def greedy_algorithm(budget, items):
    result = []
    calories = 0
    budget_used = 0

    for item in sorted(items.items(), key=lambda x: x[1]["cost"] / x[1]["calories"]):
        if item[1]["cost"] <= budget:
            result.append(item[0])
            budget -= item[1]["cost"]
            budget_used += item[1]["cost"]
            calories += item[1]["calories"]

    return {
        "result": result,
        "calories": calories,
        "budget_used": budget_used,
    }


print(greedy_algorithm(100, items))


def dynamic_programming(budget, items):
    items_list = list(items.items())
    n = len(items_list)
    table = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for w in range(budget + 1):
            if i == 0 or w == 0:
                table[i][w] = 0
                continue

            item_value = items_list[i - 1][1]
            if item_value["cost"] <= w:
                table[i][w] = max(
                    table[i - 1][w],
                    table[i - 1][w - item_value["cost"]] + item_value["calories"],
                )
            else:
                table[i][w] = table[i - 1][w]

    result = []
    calories = 0
    budget_used = 0

    i, w = n, budget
    while i > 0 and w > 0:
        if table[i][w] != table[i - 1][w]:
            item = items_list[i - 1]
            result.append(item[0])
            w -= item[1]["cost"]
            budget_used += item[1]["cost"]
            calories += item[1]["calories"]
        i -= 1

    return {
        "result": result,
        "calories": calories,
        "budget_used": budget_used,
    }


print(dynamic_programming(100, items))
