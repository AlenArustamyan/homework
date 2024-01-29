#Create a dictionary of book titles and their authors. Write a function to search for a book
#by its title and return the author's name.
def find_author_by_title(book_dict, title):
    if title in book_dict:
        return book_dict[title]
    else:
        return None

# Example usage:
books = {
    "python": "java",
    "c++": "ddd"
}

title_to_search = "python"

author = find_author_by_title(books, title_to_search)

if author:
    print({title_to_search},{author})
else:
    print({title_to_search})
