def show_hidden_word(secret_word, old_letters_guessed):
	
	
	secret_word_hidden = []
	
	for i in range (len(secret_word)):
		found = False
		for k in range(len(old_letters_guessed)):
			if secret_word[i] == old_letters_guessed[k]:
				found = True
				secret_word_hidden.append(secret_word[i])
		if found == False:
			secret_word_hidden.append("_")
			
	str_secret_word_hidden = " ".join(secret_word_hidden)
	return str_secret_word_hidden
	
def main():
	print (show_hidden_word("song",['s', 'a' ]))
	
if __name__ == "__main__":
	main()
	