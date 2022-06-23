import math
n,m,a = map(int, input().split())

lengthAmount = math.ceil(n/a)
heightAmount = math.ceil(m/a)

print(lengthAmount * heightAmount)
