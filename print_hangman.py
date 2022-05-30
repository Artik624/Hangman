def print_hangman(num_of_tries):
	num_of_tries = input("choose a number 1-9 : ")
	HANGMAN_PHOTOS = {}

	HANGMAN_PHOTOS['stage_1'] = """
		x-------x
	"""

	HANGMAN_PHOTOS['stage_2'] = """
	
		x-------x
		|
		|
		|
		|
		|
	"""
	
	HANGMAN_PHOTOS['stage_3'] = """ 
		x-------x
		|       |
		|       0
		|
		|
		|
	"""      

	HANGMAN_PHOTOS['stage_4'] = """ 
		x-------x
		|       |
		|       0
		|
		|
		|	
	"""
	HANGMAN_PHOTOS['stage_5'] = """ 
		x-------x
		|       |
		|       0
		|
		|
		|
	"""
		
	HANGMAN_PHOTOS['stage_6'] = """ 
		x-------x
		|       |
		|       0
		|       |
		|
		|
	"""	
		
	HANGMAN_PHOTOS['stage_7'] = """ 
		x-------x
		|       |
		|       0
		|      /|/
		|
		|	
	"""	
		
	HANGMAN_PHOTOS['stage_8'] = """ 	
		x-------x
		|       |
		|       0
		|      /|/
		|      /
		|
	"""

	HANGMAN_PHOTOS['stage_9'] = """ 
		x-------x
		|       |
		|       0
		|      /|/
		|      / /
		|
	"""
	
	
	
	
	
	
	

	if num_of_tries == '1':
		print(HANGMAN_PHOTOS['stage_1'])

	if num_of_tries == '2':
		print(HANGMAN_PHOTOS['stage_2'])
		
	if num_of_tries == '3':
		print(HANGMAN_PHOTOS['stage_3'])
		
	if num_of_tries == '4':
		print(HANGMAN_PHOTOS['stage_4'])
		
	if num_of_tries == '5':
		print(HANGMAN_PHOTOS['stage_5'])
		
	if num_of_tries == '6':
		print(HANGMAN_PHOTOS['stage_6'])
		
	if num_of_tries == '7':
		print(HANGMAN_PHOTOS['stage_7'])
		
	if num_of_tries == '8':
		print(HANGMAN_PHOTOS['stage_8'])
		
	if num_of_tries == '9':
		print(HANGMAN_PHOTOS['stage_9'])
	
	
def main ():
	print(print_hangman(""))
	
if __name__ == "__main__":
	main()
	