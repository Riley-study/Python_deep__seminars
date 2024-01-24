# data = {10, 9, 8, 1, 6, 3}
# data2 = [2, 3, 4, 5, 6, 7, 8]

# a, b, c, *d, e = data
# print(a, b, c, d, e)

# list_iter = iter(data2)
# print(*list_iter)


data = {2, 4, 4, 6, 8, 10, 12}
res1 = {None: item for item in data if item > 4}
res2 = (item for item in data if item > 4)
res3 = [[item] for item in data if item > 4]
print(res1, res2, res3)