#index  0   1   2   3   4   5   6
num = [10, 11, 34, 65, 63, 87, 90]
#index -7  -6  -5  -4  -3  -2  -1

for n in num:
    if n % 2 == 0:
        print(n,end=" ")
print("")
ans = [n for n in num if n % 2 == 0]
print(ans)

