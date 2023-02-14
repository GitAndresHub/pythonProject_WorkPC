def remove_duplicates():
    a = [2, 45, 6, 6, 8, 34, 34, 34, 8, 10, 3]
    c = set(a)
    d = list(c)
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    print(b)
    print(d)


remove_duplicates()