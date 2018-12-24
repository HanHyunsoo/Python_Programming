tree = [" " * (9 - x) + "*" * (2 * x - 1) for x in range(1, 10)]
print(" " * 8 + "*\n" + " " * 7 + "***\n" + " " * 8 +"*")
for i in tree[:5]:
        print(i)
for j in range(3):
    for k in tree[3 + j:7 + j]:
        print(k)
print(tree[2] + "\n" + tree[2])
print("★Merry christmas★")
