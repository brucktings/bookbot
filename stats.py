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
