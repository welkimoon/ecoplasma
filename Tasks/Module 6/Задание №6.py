search_for = set([x for x in input("Последовательность: ").split()])
search_in = set([x for x in input("Последовательность: ").split()])

print(" ".join(set.intersection(search_for, search_in)))