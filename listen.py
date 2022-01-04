# Python program to translate
# speech to text and text to speech


import speech_recognition as sr


# Initialize the recognizer
r = sr.Recognizer()

# Function to convert text to
# speech
x = 1
while(x == 1):
	
	# Exception handling to handle
	# exceptions at the runtime
	try:
		
		# use the microphone as source for input.
		with sr.Microphone() as source2:
			
			# wait for a second to let the recognizer
			# adjust the energy threshold based on
			# the surrounding noise level
			r.adjust_for_ambient_noise(source2, duration=0.2)
			print("speak..")
			#listens for the user's input
			audio2 = r.listen(source2)
			# Using ggogle to recognize audio
			MyText = r.recognize_google(audio2)
			MyText = MyText.lower()
			x = x+1
			print("Did you say "+MyText)


			
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
		
	except sr.UnknownValueError:
		print("unknown error occured")

'''
def hear():
	
	# Exception handling to handle
	# exceptions at the runtime
	try:
		
		# use the microphone as source for input.
		with sr.Microphone() as source2:
			
			# wait for a second to let the recognizer
			# adjust the energy threshold based on
			# the surrounding noise level
			r.adjust_for_ambient_noise(source2, duration=0.2)
			print("speak..")
			#listens for the user's input
			audio2 = r.listen(source2)
			# Using ggogle to recognize audio
			u_input = r.recognize_google(audio2)
			u_input = u_input.lower()

			print("Did you say "+u_input)


			
	except sr.RequestError as e:
		print("Could not request results; {0}".format(e))
		
	except sr.UnknownValueError:
		print("unknown error occured")
		'''