
# this is for counting number of words in sentence/paragraph
def CountWords(words):
	if words is not None:
		NumberOfWords = [Eachword.count(' ') + 1 for Eachword in words]
		return NumberOfWords
