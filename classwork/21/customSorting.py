data = [("A", 80, 20), ("B", 90, 18)]

for i in range(len(data)):
    for j in range(i+1, len(data)):
        if data[i][1] < data[j][1] or \
           (data[i][1] == data[j][1] and data[i][2] > data[j][2]):
            data[i], data[j] = data[j], data[i]

print(data)
