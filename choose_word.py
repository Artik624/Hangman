def choose_word(file_path, index):
	file_path = input("Type the path of the file you want to play with : ")
	index = int(input("Choose the index of the word that you want to guess : "))
	print("\n")
	index = index - 1
	words_list = []
	seperator = ""
	with open (file_path, 'r') as opened_file:
		content = opened_file.read()
		words_list = content.split(" ")
		words_list = list(dict.fromkeys(words_list))
	if seperator in words_list:
		words_list.remove(seperator)
		
	while index > len(words_list) :
		index = index - (len(words_list))
		
		
	



	return words_list[index]



