from stats import num_words

def get_book_text(path_to_file):
	with open(path_to_file) as f:
		text = f.read()
	return text


def main():
	full_text = get_book_text('books/frankenstein.txt')
	print(f"{num_words(full_text)} words found in the document")
main()