def case_convers(s):
    queue =list(s)
    nw_queue = []
    lc_count = 0
    uc_count = 0
    for case in queue:
        if case.isupper():
            uc_count +=1
        elif case.islower():
            lc_count +=1

    if uc_count>lc_count:
        for case in queue:
            nw_queue.append(case.upper())
    elif uc_count<lc_count:
        for case in queue:
            nw_queue.append(case.lower())
    elif uc_count == lc_count:
        for case in queue:
            nw_queue.append(case.lower())

    return ''.join(nw_queue)



s = input()
result = case_convers(s)
print(result)