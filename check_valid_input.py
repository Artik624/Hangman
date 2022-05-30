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
		
	
	
def choose_letter():
	letter_guessed = input("Choose a letter : ")
	return letter_guessed.lower()
	
	
	

def main():
	letter = choose_letter()
	print(check_valid_input(letter, [] ))
	

if __name__ == "__main__":
	main()