def is_valid_input(letter_guessed):
	"""
	recieves a letter nd verifies if it according to the standards
	:param letter_guessed:the letter that the the user provides
	:type: str
	:return: true or false
	:rtype: boolian
	"""
	letter_guessed = input("Guess a letter: ")
	import re

	if len(letter_guessed) != 1 or not re.match("^[a-zA-Z]*$" ,letter_guessed):
	#return false if the input is anything but a single english letter
		t_or_f =  False
	else :
		t_or_f =  True 
	
	return (t_or_f, letter_guessed)
def main():
	
	print (is_valid_input(""))
	
if __name__ == "__main__":
    main()