from collections import Counter

avg = 0
names = []
company = Counter()
sub_company = Counter()

n = int(input())
for _ in range(n):
    name = input()
    names.append(name)
    sub_avg = 0
    for _ in range(4):
        i = int(input())
        avg += i
        sub_avg += i
    company[name] = sub_avg

avg /= n
print(round(avg))
for i in names:
    if company[i] - avg > 0:
        print(i, end=" ")
print()
for i in names:
    if company[i] - avg < 0:
        print(i, end=" ")