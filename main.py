import sys
from stats import num_words, num_chars, sorted_chars

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    #Get book text from file
    with open(filepath) as f:
        return f.read()

def main():
    book_text = get_book_text(sys.argv[1])
    word_count = num_words(book_text)
    char_count = sorted_chars(num_chars(book_text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in char_count:
        print(f"{item['char']}: {item['count']}")
    print("============= END ===============")

main()

