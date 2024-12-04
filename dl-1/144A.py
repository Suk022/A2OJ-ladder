def find_max_min_to_positions(s):

    queue = list(map(int, s))

    max_element = queue[0]
    min_element = queue[0]
    max_index = 0
    min_index = 0

    for i in range(len(queue)):
        if queue[i] > max_element:
            max_element = queue[i]
            max_index = i
        if queue[i] < min_element:
            min_element = queue[i]
            min_index = i

    while max_index > 0:
        queue[max_index], queue[max_index - 1] = queue[max_index - 1], queue[max_index]
        max_index -= 1

    if min_index < max_index:
        min_index += 1

    while min_index < len(queue) - 1:
        queue[min_index], queue[min_index + 1] = queue[min_index + 1], queue[min_index]
        min_index += 1

    return queue


s = input("Enter space-separated values: ").split()
result = find_max_min_to_positions(s)
print(result)
