#Write a function that takes two lists and returns a new list containing only the common
#elements. (without using set)


def find_elements(list1, list2):
    common_elements = [element for element in list1 if element in list2]
    return common_elements

list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]

result = find_elements(list_a, list_b)
print(result)
