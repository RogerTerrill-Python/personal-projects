data_list = [d for d in range(10)]
print(data_list)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

data_dict = {d: d for d in data_list}
print(data_dict)  # {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}

interesting_points = []

interesting_ids = {1, 4, 6, 7}

for d_id in interesting_ids:
    d = data_dict[d_id]
    interesting_points.append(d)

print(interesting_points)