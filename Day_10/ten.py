import fileinput
import re

p1 = 0
p2 = 0

xs = [int(x) for x in list(fileinput.input())]
xs.append(0)
xs = sorted(xs)
xs.append(max(xs)+3)
n1 = 0
n3 = 0
for i in range(len(xs)-1):
    d = xs[i+1]-xs[i]
    if d==1:
        n1 += 1
    elif d==3:
        n3 += 1

DP = {}
def dp(i):
    if i==len(xs) -1:
        return 1
    if i in DP:
        return DP[i]
    ans = 0
    for j in range(i+1, len(xs)):
        if xs[j]-xs[i]<=3:
            ans += dp(j)
    DP[i] = ans
    return ans
    
print("Part 1: ")
print(n1 * n3)
print("Part 2: ")
print(dp(0))