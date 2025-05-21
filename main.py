import sys
from stats import word_count, character_count, sorted_list_of_dictionaries


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    wrd_count = word_count(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {wrd_count} total words")
    print("--------- Character Count -------")
    char_dict = character_count(text)
    sorted_list_of_dictionaries(char_dict)
    print("============= END ===============")


main()
