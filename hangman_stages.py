def hangman_stages(stage_int):
	
	
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
		HANGMAN_PHOTOS['stage_4'] =""" 
			 
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
			
		
		
	
	
def main():
	
	print(hangman_stages(2))
	

if __name__ == "__main__":
	main()
	
