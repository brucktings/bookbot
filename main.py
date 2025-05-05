import stats

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        text = f.read()
    return text

def main():
    full_text = get_book_text('books/frankenstein.txt')
    
    # Get word count and character counts
    word_count = stats.num_words(full_text)
    char_counts = stats.char_count(full_text)
    sorted_chars = stats.sort_char_count(char_counts)
    
    # Print the report
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
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