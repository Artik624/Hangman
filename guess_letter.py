guessed_letter = input ("Guess a letter :" )
guessed_letter = str ( guessed_letter.lower() )
letter_length = int(len(guessed_letter))

import re

 wrong_input = "X"

if letter_length > 1 and re.match("^[a-z]*$" ,guessed_letter):
	return wrong_input
elif  letter_length == 1 and not re.match("^[a-z]$" ,guessed_letter) :
	return wrong_input
	
elif letter_length > 1 and not re.match("^[a-z]*$" ,guessed_letter)  :
	return wrong_input
	
else :
	return guessed_letter
