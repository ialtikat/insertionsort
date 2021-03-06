def insertionsort(self):
    for i in range(1, len(self)):
        value = self[i]
        while i > 0 and self[i - 1] > value:
            self[i] = self[i - 1]
            i = i-1
        self[i] = value
    return self
array=[12, 6, 81, 48, 23, 67]
print(insertionsort(array))


#    Output
# -> [6, 12, 23, 48, 67, 81]


