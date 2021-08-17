a = []
for i in range(int(input())):
    a.append(int(input()))

max_1 = max(a[0], a[1])
min_1 = min(a[0], a[1])
max_2 = a[0] * a[1]
min_2 = a[0] * a[1]
max_3 = a[0] * a[1] * a[2]

for x in a[2:]:
    max_3 = max(max_3, x * max_2, x * min_2)
    max_2 = max(max_2, x * max_1, x * min_1)
    min_2 = min(min_2, x * max_1, x * min_1)
    max_1 = max(max_1, x)
    min_1 = min(min_1, x)

print(max_3)