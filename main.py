def get_book_text(path_to_file):
	with open(path_to_file) as f:
		text = f.read()
	return text

def num_words(path_to_file, encoding='utf-8'):
	text = get_book_text(path_to_file)
	words = text.split()
	return len(words)

def main():
    print(f"{num_words('books/frankenstein.txt')} words found in the document")
main()