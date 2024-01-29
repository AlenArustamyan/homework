#Write a function that returns the nth largest element from a list.

def nth_largest_element(lst, n):
    if n <= 0:
        print("Invalid value of n.")
        return None

    sorted_list = sorted(lst, reverse=True)

    if 1 <= n <= len(sorted_list):
        nth_largest = sorted_list[n - 1]
        return nth_largest
    else:
        print("Invalid value of n.")
        return None
my_list = [10, 5, 8, 20, 15]
n_value = 2

result = nth_largest_element(my_list, n_value)

if result is not None:
    print({n_value},{result})

