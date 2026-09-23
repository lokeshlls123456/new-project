n = int(input())
primary_sum = 0
secondary_sum = 0

for i in range(n):
    row = list(map(int, input().split()))
    primary_sum += row[i]           
    secondary_sum += row[n - 1 - i] 
print(primary_sum, secondary_sum)