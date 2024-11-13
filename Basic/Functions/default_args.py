def sum (a, b, c=0, d=0):
    ans = a + b
    return ans

print(sum(10,23))



def all_sum (a, b, *args):
    print(f"{a} {b}")
    sum = 0
    for i in args:
        sum += i
    return sum


print(all_sum(1, 2, 3, 4, 5, 6))