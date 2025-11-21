file = open("sport.txt", "r", encoding="cp1251")
s = file.readlines()

madict = dict()
for line in s:
    line = line.replace(" , ", ", ")
    line = line.split("\t")
    lst = line[3].split(", ")
    for sp in lst:
        if sp != "":
            sp = sp.lower()
            madict[sp] = madict.get(sp, 0) + 1


a = sorted(madict, key=madict.get, reverse=True)
print(a[0], madict[a[0]])
print(a[1], madict[a[1]])
print(a[2], madict[a[2]])
