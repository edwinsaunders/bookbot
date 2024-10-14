# function to supply a key for sorting for the .sort() method
def sort_on(dict):
	return dict["count"]


# function to get individual letter counts and return them in a dictionary
def getCharCounts(string):
	string = string.lower()

	count_dict = {}

	for char in string:
		if char.isalpha():
			if char in count_dict:
				count_dict[char] += 1
			else:
				count_dict[char] = 1

	return count_dict


def main():

	# open a book file
	with open("books/frankenstein.txt") as f:
		file_contents = f.read()

	# split up the file into a list of words
	word_list = file_contents.split()
	

	# count the words in the book
	word_count = len(word_list)

	# get the individual character counts
	char_dict = getCharCounts(file_contents)
	
	# turn char_dict into a list of dictionaries for sorting by count
	dict_list = []
	for char in char_dict:
		single_dict = {}
		single_dict["letter"] = char
		single_dict["count"] = char_dict[char]
		dict_list.append(single_dict)

	# sort by count descending using key function sort_on
	dict_list.sort(reverse=True, key=sort_on)

	# print formatted output to stdout

	print("--- Begin report of books/frankenstein.txt ---")
	print(f"{word_count} words found in the document\n")
	
	
	for d in dict_list:
		letter = d["letter"]
		count = d["count"]
		print(f"The '{letter}' character was found {count} times")

main()