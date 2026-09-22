n = int(input().strip())
product_ids = list(map(int, input().strip().split()))
newProductId = int(input().strip())
inserted = False
for i in range(n):
    if newProductId <= product_ids[i]:
        product_ids.insert(i, newProductId)
        inserted = True
        break
if not inserted:
    product_ids.append(newProductId)
print(" ".join(map(str, product_ids)))