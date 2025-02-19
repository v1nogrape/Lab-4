from itertools import combinations

start_points = 15
max_size = 8  #2x4
items = {
    'r': (3, 25), 'p': (2, 15), 'a': (2, 15), 'm': (2, 20), 'i': (1, 5),
    'k': (1, 15), 'x': (3, 20), 't': (1, 25), 'f': (1, 15), 'd': (1, 10),
    's': (2, 20), 'c': (2, 20)
}

def get_totals(selected):
    size = sum([items[item][0] for item in selected])
    points = sum([items[item][1] for item in selected]) + start_points
    return size, points

max_points = float('-inf')
best_combo = ()
for size in range(1, len(items) + 1):
    for combo in combinations(items.keys(), size):
        total_size, total_points = get_totals(combo)
        if total_size <= max_size and total_points > max_points:
            max_points = total_points
            best_combo = combo

inventory = [[" " for _ in range(4)] for _ in range(2)] #2x4
index = 0
for item in best_combo:
    for _ in range(items[item][0]):
        if index < max_size:
            inventory[index // 4][index % 4] = f"[{item}]"
            index += 1

for row in inventory:
    print(",".join(row))
print("Итоговые очки выживания:", max_points)