num = int(input("Enter one integer: "))

col1 = 1
col2 = num

print(col1, col2)

for i in range(1, num):
    col1 += 1
    col2 -= 1
    print(col1, col2)