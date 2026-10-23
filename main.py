import sys
from stats import check_lines, find_best

lines = sys.stdin.read().splitlines()
total, count = check_lines(lines)
best = find_best(total, count)

print(len(lines))
print(0)
print(total[best] / count[best])