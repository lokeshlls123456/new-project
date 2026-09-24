n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
is_upper = True
for i in range(n):
    for j in range(i):  
        if matrix[i][j] != 0:
            is_upper = False
            break
    if not is_upper:
        break
if is_upper:
    print("Upper triangular matrix")
else:
    print("Not an Upper triangular matrix")