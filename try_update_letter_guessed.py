def check_valid_input(letter_guessed, old_letters_guessed):
	"""
	recieves a letter and verifies if it according to the standards
	:param letter_guessed:the letter that the the user provides
	:type: str
	:param old_letters_guessed: the list of already guessed letter
	:type: str
	:return: true or false
	:rtype: boolian
	"""
	
	
	import re
		
	
	if len(letter_guessed) != 1 or not re.match("^[a-zA-Z]*$" ,letter_guessed) \
	or letter_guessed in old_letters_guessed:
	#return false if the input is anything but a single english letter that hasent been guessed already
		return False
	else:
		return True
		

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
	"""
	recieves a letter and verifies if it according to the standards , adds it to a list of already guessed letters
	:param letter_guessed:the letter that the the user provides
	:type: str
	:param old_letters_guessed: the list of already guessed letter
	:type: str
	:return: true or false
	:rtype: boolian
	"""
	
	
	
	import re
		
	
	if check_valid_input(letter_guessed, old_letters_guessed) == False:
	#return false if the input is anything but a single english letter that hasent been guessed already
		print ("X")
		arrow = " -> "
		output =  arrow.join((sorted(old_letters_guessed)))
		flag =  False
	else:
		old_letters_guessed.append(letter_guessed)
		old_letters_guessed = sorted(old_letters_guessed)
		
		flag =  True
		
	if flag == False:
		return output
	else:
		from show_hidden_word import show_hidden_word
		show_hidden_word()
	
		
	
	
