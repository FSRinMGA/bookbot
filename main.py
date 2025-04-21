import sys 
from stats import get_num_words, get_num_chars, get_sorted_chars

def get_book_text(filepath):
    file_contents = ""
    with open(filepath) as f:
        file_contents = f.read()
    num_words = get_num_words(file_contents)
    num_chars = get_num_chars(file_contents)
    sorted_chars = get_sorted_chars(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_chars:
        print(entry)
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    get_book_text(sys.argv[1])
    return 0

main()