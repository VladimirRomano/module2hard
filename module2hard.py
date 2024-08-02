import random


def numbers():
     n = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
     res = random.choice(n)
     return res

res = numbers()
print(res)
p2 = []
for i in range(1, 21):
     for j in range(2, 21):
          s1 = i + j
          p1 = [i, j]
          if s1 == res or res % s1 == 0:
               p2.append(p1)

print(*p2)
