#Write a function that performs the following tasks:
#Accepts a list and an index as input.
#Attempts to access the element at the given index in the list.
#Handles both IndexError
#Uses a finally block to print "Task completed" regardless of whether an exception
#occurred or not


def access_element_at_index(my_list, index):
    try:
        result = my_list[index]
        print("Element at index", index, ":", result)
    except IndexError:
        print("IndexError:")
    finally:
        print("completed")
my_list = [1, 2, 3, 4, 5]
index_to_access = 3
access_element_at_index(my_list, index_to_access)
