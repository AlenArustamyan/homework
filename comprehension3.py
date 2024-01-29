#Create a list of vowels present in a given word.

def vowels(word):
    vowels1 = ['a', 'e', 'i', 'o', 'u']
    vowel_list = [char for char in word.lower() if char in vowels1]
    return vowel_list

# Example usage:
input_word = "Hello"

result_vowels = vowels(input_word)
print(vowels)
