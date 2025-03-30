def num_words(text):
    # Count the number of words in the book
    return len(text.split())

def num_chars(text):
    # Count the number of characters in the book
    text = text.lower()
    characters = {}
    for char in text:
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sorted_chars(characters):
    # Function to sort characters
    # Firstly add into a tuple
    list_dicts = []
    for char, count in characters.items():
        if char.isalpha():
            list_dicts.append({"char": char, "count": count})
    list_dicts.sort(reverse = True, key = sort_on) 
    return list_dicts
        
def sort_on(dict):
    return dict["count"]

# TEMP TEST
# test_text = "Hello world! This is a test text."
# print(sorted_chars(num_chars(test_text)))