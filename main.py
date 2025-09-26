import sys
from stats import *

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    breakdown = breakdown_of(
        get_book_text(sys.argv[1])
        )
    count_of_words = count_words_in_book(
        get_book_text(
            sys.argv[1]
            )
        )
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {count_of_words} total words")
    print("--------- Character Count -------")
    for item in sorted_character_list(dictionary_to_sortable(breakdown)):
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()