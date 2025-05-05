def num_words(text):
	words = text.split()
	return len(words)

def char_count(text):
	counts = {}
	for char in text.lower():
		if char in counts:
			counts[char] += 1
		else:
			counts[char] = 1
	return counts

def sort_char_count(counts):
    # Create an empty list to store our dictionaries
    chars_list = []
    
    # Loop through each character and its count in the dictionary
    for char, count in counts.items():
        # Create a dictionary for this character
        char_dict = {"char": char, "num": count}
        # Add it to our list
        chars_list.append(char_dict)
    
    # Now sort the list by the "num" value
    def sort_on(dict_item):
        return dict_item["num"]
    
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list