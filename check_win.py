def check_win(secret_word, old_letters_guessed):
	secret_word = secret_word.lower()
	count = 0
	
	for i in range (len(secret_word)):
		if secret_word[i] in old_letters_guessed:
				count += 1
				
				
	if count == len(secret_word):	
		return True
	else:
		return False
		
	
	
