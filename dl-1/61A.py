def check_pair(first_pair, second_pair):

    result = []

    for i in range(len(first_pair)):
        result.append('1' if first_pair[i] != second_pair[i] else '0')

    return ''.join(result)

first_pair = input()
second_pair = input()
res = check_pair(first_pair,second_pair)
print(res)