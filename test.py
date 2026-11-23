import sys

input = sys.stdin.readline

n, m = map(int, input().split())

d = {0: 0}


def add_segment(left, right):
    d[left] = d.get(left, 0) + 1
    d[right] = d.get(right, 0) - 1


for i in range(n):
    x, y = map(int, input().split())

    r = y % m

    if r == 0:
        continue

    end = x + r

    if end <= m:
        add_segment(x, end)
    else:
        add_segment(x, m)
        add_segment(0, end - m)

current = 0
best = -1
answer = 0

for position in sorted(d):
    if position == m:
        break

    current += d[position]

    if current > best:
        best = current
        answer = position

print(answer)