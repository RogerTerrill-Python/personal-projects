import collections
import random

import sys

DataPoint = collections.namedtuple("DataPoint", "id")


def main():
    # #############################
    print("Creating data...\n", end=' ')
    sys.stdout.flush()

    data_list = []  # 50 DataPoint items
    random.seed(0)
    for d_id in range(50):
        data_list.append(DataPoint(d_id))

    print(f'The Data_list is {data_list} \n')

    interesting_ids = {random.randint(0, len(data_list)) for _ in range(0, 5)}
    print(f'Interesting_ids are {interesting_ids} \n')

    interesting_points = []

    # 1. Create dictionary via comprehension, key = id

    data_dict = {d.id: d for d in data_list}
    print(f'The dict is:  {data_dict} \n')

    # 2. locate the data in dictionary
    for d_id in interesting_ids:
        d = data_dict[d_id]
        interesting_points.append(d)

    print(interesting_points)



if __name__ == '__main__':
    main()
