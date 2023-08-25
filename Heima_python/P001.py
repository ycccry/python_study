a = [1,2,3]
b = [11,22,33]
c = [a,b]
d = c.copy()
e = c
print(id(c))
print(id(d))
print(id(e))

d[0] = [5,6,7]

print(c)