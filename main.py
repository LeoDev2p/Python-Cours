d = {}
for n in [1, 2, 3, 4]:
    d.setdefault(n % 2, []).append(n)

print (d)