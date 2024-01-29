#Write a function that checks if two sets are disjoint (have no common elements)

def are_disjoint(set1, set2):
    return set1.isdisjoint(set2)

set_a = {1, 2, 3, 4}
set_b = {5, 6, 7}

result = are_disjoint(set_a, set_b)

if result:
    print("The sets are disjoint.")
else:
    print("The sets have common elements.")
