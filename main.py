import sys

from stats import counting_words
from stats import counting_characters
from stats import ranger

def get_book_test(filepath):

    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) == 2:
        link = sys.argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {link}...")
        print("----------- Word Count ----------")
        print(f"Found {counting_words(get_book_test(link))} total words")
        print("--------- Character Count -------")
        sorted_list = ranger(counting_characters(get_book_test(link)))
        for i in sorted_list:
            print(f"{i['char']}: {i['num']}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return

main()
