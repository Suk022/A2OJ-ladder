def word_long_or_not(queue):
 for word in queue:
        if len(word) <=10 :
            print(word)
        else:
            first_element = word[0]
            last_element = word[-1]
            count = len(word) - 2
            print(f"{first_element}{count}{last_element}")


n = int(input())
queue = []

for _ in range(n):
    s =input()
    queue.append(s)

word_long_or_not(queue)