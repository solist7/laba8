spisok = [float(x) for x in input().split()]
d = float(input())
average_of_numbers = sum(spisok)/len(spisok)
count = 0
for x in spisok:
    if abs(x - average_of_numbers) <= d:
        count +=1
print(count)
