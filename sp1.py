# 16
# 12.10.2026
# kmitání kuličky tam a zpět
import math
import time
print("Zadej počet:")
pocet = int(input())
print("Kulička jede")
for i in range(pocet):
    time.sleep(0.1)
    print(" " * i + "O")

for i in range(pocet - 2, -1, -1):
    time.sleep(0.1)
    print(" " * i + "O")

print("Tabulka")
for i in range(1, pocet + 1):
    print(i, i * i, math.sqrt(i))
