l = [0, 1, 2, 7]
l = sorted(l)
print(l)
k = []
for i in range(1, len(l)):
    print(l[i-1], l[i])
    k.append((l[i-1]+l[i])/2)
    
print(k)
