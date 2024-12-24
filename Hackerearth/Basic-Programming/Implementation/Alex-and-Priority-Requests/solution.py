import sortedcontainers

time_to_priority_map = {}
priority_set = sortedcontainers.SortedList()


def add(time, priority):
    time_to_priority_map[time] = priority
    priority_set.add(priority)


def delete(time):
    if time in time_to_priority_map:
        priority = time_to_priority_map[time]
        priority_set.remove(priority)
        del time_to_priority_map[time]


def main():
    query_count = int(input())
    for _ in range(query_count):
        query_type = int(input())
        if query_type == 1:
            time, priority = map(int, input().split())
            delete(time)
            add(time, priority)
        elif query_type == 2:
            time = int(input())
            delete(time)
        elif query_type == 3:
            print(priority_set[0], priority_set[-1])
        else:
            print(time_to_priority_map[max(time_to_priority_map.keys())])


if __name__ == "__main__":
    main()
