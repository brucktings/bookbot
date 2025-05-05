import sys
import stats

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    path_to_book = sys.argv[1]


def get_book_text(path_to_book):
    with open(path_to_book) as f:
        text = f.read()
    return text

def main():
    full_text = get_book_text(path_to_book)
    
    # Get word count and character counts
    word_count = stats.num_words(full_text)
    char_counts = stats.char_count(full_text)
    sorted_chars = stats.sort_char_count(char_counts)
    
    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")  # Use the variable, not the function call
    print("--------- Character Count -------")
    
    for char_dict in sorted_chars:
        char = char_dict["char"]
        if char.isalpha():  # Only print alphabetic characters
            print(f"{char}: {char_dict['num']}")
    
    print("============= END ===============")

# Call the main function
main()