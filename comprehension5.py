#Given a list of words, create a dictionary where keys are words, and values are
#their lengths, but only for words with lengths greater than 3.

def create_word_length_dict(words):
    word_length_dict = {}

    for word in words:
        if len(word) > 3:
            word_length_dict[word] = len(word)

    return word_length_dict

word_list = ["apple", "banana", "orange", "kiwi", "pear"]

result_dict = create_word_length_dict(word_list)
print( result_dict)
