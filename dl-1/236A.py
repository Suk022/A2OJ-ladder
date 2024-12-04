def distinct_letter(string):
    arr = list(string)
    distinct_letter_arr = []
    for char in arr:
        if char not in distinct_letter_arr:
            distinct_letter_arr.append(char)

    distinct_no = len(distinct_letter_arr)
    if distinct_no % 2 == 0 :
        return 'CHAT WITH HER!'
    else:
        return 'IGNORE HIM!'

string = input().lower()
res = distinct_letter(string)
print(res)