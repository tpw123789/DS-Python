
data = [16, 25, 13, 78, 45, 56, 21, 17]


def select(elements):
    for i in range(len(elements) - 1):
        for j in range(i + 1, len(elements)):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
        print(elements)


select(data)
print(data)
