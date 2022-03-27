
data = [16, 25, 13, 78, 45, 56, 21, 17]

print('start sorting', data)

for i in range(len(data) - 1, -1, -1):
    for j in range(i):
        if data[j] > data[j + 1]:
            data[j], data[j + 1] = data[j + 1], data[j]

    print(f'第{len(data) - i}次結果是:', data)
