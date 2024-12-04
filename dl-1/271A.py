def has_distinct_digits(year):
    digits = list(str(year))
    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            if digits[i] == digits[j]:
                return False
    return True

def next_distinct_year(year):
    year += 1
    while not has_distinct_digits(year):
        year += 1
    return year

year = int(input())
print(next_distinct_year(year))
