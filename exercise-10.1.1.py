def welcome_page():													# prints the welcome page
	"""
	receives no parameters and print the welcome page and the amount of tries the player has.
	"""
	global MAX_TRIES 
	MAX_TRIES = 7

	HANGMAN_ASCII_ART =("""

	  _    _                                         
	 | |  | |                                        
	 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
	 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
	 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
	 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
			      _ / |                      
			     |___/
	""")



	print (HANGMAN_ASCII_ART , "you have" , MAX_TRIES , " tries" )
	
 
def hangman_stages(stage_int):										# has all the stages of the hangman 
	"""	
	recieves a number to identify which stage of hangman to print
	:param stage_int:the number thaat identifies the stage
	:type:int
	:return:the correct stage of the hangman
	:rtype:dictionary
	"""
	
	HANGMAN_PHOTOS = {}
	if stage_int == 1:
		HANGMAN_PHOTOS['stage_1'] = "x-------x"
		return HANGMAN_PHOTOS['stage_1']
		
		
	if stage_int == 2:
		HANGMAN_PHOTOS['stage_2'] =""" 
		
			x-------x
			|
			|
			|
			|
			|
		"""
		return  HANGMAN_PHOTOS['stage_2']



	if stage_int == 3:
		HANGMAN_PHOTOS['stage_3'] = """
		
			x-------x
			|       |
			|       0
			|
			|
			|
		"""      
		return HANGMAN_PHOTOS['stage_3']
		
		
	if stage_int == 4:
		HANGMAN_PHOTOS['stage_4'] = """
		
			x-------x
			|       |
			|       0
			|       |
			|
			|
		"""      
		return HANGMAN_PHOTOS['stage_4']
	
	if stage_int == 5:	
		HANGMAN_PHOTOS['stage_5'] ="""
			
				x-------x
				|       |
				|       0
				|      /|/
				|
				|	
			"""	
		return HANGMAN_PHOTOS['stage_5']
	
	if stage_int == 6:	
		HANGMAN_PHOTOS['stage_6'] =""" 
				
				x-------x
				|       |
				|       0
				|      /|/
				|      /
				|
			"""
		return HANGMAN_PHOTOS['stage_6']
	
	if stage_int == 7:
		HANGMAN_PHOTOS['stage_7'] =""" 
			
				x-------x
				|       |
				|       0
				|      /|/
				|      / /
				|
			"""
		return HANGMAN_PHOTOS['stage_7']		
					
			
def show_hidden_word(secret_word, old_letters_guessed):				#converts the chosen word to a hidden word and reveals letters if they are guessed correctly
	"""
	recieves a word and a list of letters and converts them to underscores unless the letter is present in the list
	:param secret_word:the word that is to be guessed
	:type:str
	:param old_letters_guessed:the list of lettes that the player inputs
	:type:list
	:return:a string of underscores or underscores & letters if guessed correctly
	:rtype:str
	"""
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


def check_valid_input(letter_guessed, old_letters_guessed):			# verifies if the input is correct
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
		
		return_statement =  False
	else:
		
		return_statement = True
		
	return return_statement
	
		
def try_update_letter_guessed(letter_guessed, old_letters_guessed):#according to the input print error message or adds it to the list of guessed letters
	"""
	recieves a letter and a list of letters , and uses function check_valid_input() to verify the input is correct 
	returns an updated list of guessed letter or returns none and error print
	:param letter_guessed:the letter that the the user provides
	:type: str
	:param old_letters_guessed: the list of already guessed letter
	:type: list
	:return: an updated old_letters_guessed or None
	:rtype: None or list
	"""
	import re
	
	
	if check_valid_input(letter_guessed, old_letters_guessed) == False:
	#return false if the input is anything but a single english letter that hasent been guessed already
			

		print ("X")
		arrow = " -> "
		output =  arrow.join((sorted(old_letters_guessed)))
		print("you tried these letters already : ", output)
		return 
		
	else:
			
		old_letters_guessed.append(letter_guessed)
		
		old_letters_guessed = sorted(old_letters_guessed)
		
		
		
		
	return old_letters_guessed
	
	
def choose_word(file_path, index):									#provides the user the option to choose a word from a text file by word index
	"""
	recieves a file directory for a text file and converts the text to a list of words & removes duplicates, 
	and chooses one word from that list by index where input 1 uquals index[0]
	:param file_path: a string input for the user for file directory
	:type:str
	:param index:the index of the word the player chooses.
	:type:int
	:return:words_list[index] the word in the list according to the index
	:rtype:str
	"""
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

def check_win(secret_word, old_letters_guessed):					#verifies if the user guessed the word
	"""
	recieves a word and a list of guessed letters to check if the word was guessed.
	:param secret_word: the word that the user needs to guess
	:type:str
	:param old_letters_guessed:list of lettes that the user guessed
	:type:list
	:return:true if word was guessed or false if not
	:rtype:boolian
	"""
	secret_word = secret_word.lower()
	count = 0
	
	for i in range (len(secret_word)):
		if secret_word[i] in old_letters_guessed:
				count += 1
				
				
	if count == len(secret_word):	
		return True
	else:
		return False
		
	
def is_correct_guess (secret_word, old_letters_guessed):			#verifies if the guessed letter is correct
	"""
	recieves a word that the user is trying to guess and a list of guessed letters, to verifiy if the guess is correct
	:param secret_word:the word that the user is trying to guess
	:type:str
	:param old_letters_guessed:the list of guessed letter
	:type:list
	:return:found - true if guess correct , otherwise false
	:rtype:boolian
	"""
	found = False
	for i in range (len(secret_word)):
		
		for k in range(len(old_letters_guessed)):
			if secret_word[i] == old_letters_guessed[k]:
				found = True

	return found
	
	
	
def hangman_game():		#the game of hangman where the user tries to guess a word by letters until he wins or runs out of tries.
	"""
	recieves no parameters , uses the functions  welcome_page() ,hangman_stages(), show_hidden_word(), try_update_letter_guessed(), choose_word(), check_win(), 
	is_correct_guess() to recieve from the user a text file and a choice of a word from the text. the user is to guess the word by letters, where each correct 
	guess will reveal the letter in the word, an incorrect guess will progress the stages of the hangman and print an output accordungly.
	the user will repeat input of a letter until he guesses the word or runs out of tries.
	:return:result - the correct output if guessed succefully or not
	:rtype:str
	"""
	
	
	welcome_page()#prints welcome page
	
	guessed_letters_list = []																# intial list of guessed letters , empty
	chosen_word = choose_word("", 0)														# calls the choose_word() function to get input from user
	chosen_word_hidden = show_hidden_word(chosen_word, guessed_letters_list)				# calls the show_hidden_word() function to hide the word
	
	print ("Lets start !\n\n{} \n \n {}".format(hangman_stages(1),chosen_word_hidden ))		# prints the first stage and the hidden word
	print("\n")

	
	num_of_tries = 1
	while check_win(chosen_word, guessed_letters_list) != True and num_of_tries < MAX_TRIES:#loops until word is guessed or runs out of tries, 
																							#each iteration the user has to input a new etter
		
		this_letter = input("Choose a letter : ").lower()									#the letter guessed by the user
		if try_update_letter_guessed(this_letter, guessed_letters_list) == None:			#if the input is incorrect reloads the loop
			print("try again ")

		else: 
			if is_correct_guess(chosen_word, this_letter) == True:							#if input is correct print  according output 
				print(show_hidden_word(chosen_word, guessed_letters_list))
			elif is_correct_guess(chosen_word, this_letter) == False:						#if input is correct but guess wrong , print according output and progress hangman stage
				num_of_tries += 1
				print(":( \n", hangman_stages(num_of_tries) )
	

	if check_win(chosen_word, guessed_letters_list) == True:#once out of the loop , verifies using check_win() if guessed the word or ran out of tries.
		result = "YOU WIN"
	else:
		result = "YOU LOST"
	
	return result

def main():
	print(hangman_game())
	

if __name__ == "__main__":
	main()