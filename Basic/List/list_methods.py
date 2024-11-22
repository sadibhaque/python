#index  0   1   2   3   4   5   6
num = [10, 11, 34, 65, 63, 87, 90]
#index -7  -6  -5  -4  -3  -2  -1


num.append(100) # appending 100 at the end of the list
print(num)

num.insert(1,9) # inserting 9 at index 1
print(num)

if 9 in num:
    num.remove(9) # removing 9 if available in list
    print(num)    

last = num.pop()  # removing the last element
print(last, num)

if 34 in num:
    idx = num.index(34) # finding the index of 34 is in the list
print(idx)

num.sort(reverse=True) # reverse sorting 
print(num)

num.reverse()
print(num)
