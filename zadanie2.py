matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


n = len(matrix)
c = n // 2
for r in range(c + 1):
    elements = []
    for i in range(c-r,c+r+1):
        for j in range(c - r , c + r + 1):
            elements.append(matrix[i][j])

    maxx = max(elements)
    mini = min(elements)
print(maxx - mini)
