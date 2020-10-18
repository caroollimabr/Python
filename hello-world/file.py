list = ['a', 1, 'b', 2]
d = dict()
for i in range(len(list)-1):
    d[list[i]] = list[i+1]
print(d['b'])