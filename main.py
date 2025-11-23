import sys
from stats import count_words, count_characters, sort_characters


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():

    # Prüfen, ob ein Argument übergeben wurde
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Das zweite Argument ist der Pfad zur Datei
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)


    # Wörter zählen
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")

    # Charaktere zählen
    chars = count_characters(book_text)
    print(chars)

    chars = count_characters(book_text)
    sorted_chars = sort_characters(chars)

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")


main()

