m, n = map(int, input().split())
sorted_count = 0
for _ in range(m):
    row = list(map(int, input().split()))
    if all(row[i] <= row[i+1] for i in range(n - 1)):
        sorted_count += 1
print(sorted_count)