#Write a function that swaps the values of two tuples.

def swap_tuple_values(tuple1, tuple2):
    tuple1, tuple2 = tuple2, tuple1
    return tuple1, tuple2

tuple_a = (1, 2)
tuple_b = (3, 4)

swaps_tuple_a, swaps_tuple_b = swap_tuple_values(tuple_a, tuple_b)

print(tuple_a)
print(tuple_b)
print(swaps_tuple_a)
print(swaps_tuple_b)

