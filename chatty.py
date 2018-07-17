import random
import wikipedia
import sqlstuff
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")


# The AI's Power Switch is set to On (1) by Default
power_switch = 1
user_name = "Me"
ai_name = "Bob"

greetings = ['hola', 'hello', 'hi', 'Hi', 'hey!','hey']
random_greeting = random.choice(greetings)

question = ['How are you?','How are you doing?']
responses = ['Okay',"I'm fine"]
random_response = random.choice(responses)

# The AI is allowed to keep going as long as their power is over 0.
while power_switch > 0:
	print(random_greeting)
	print("You are still playing, because your power is %d." % power_switch)
	userInput = input(">>> ")
	if userInput in greetings:
		print(random_greeting)
		speaker.Speak(random_greeting)
	elif userInput not in question:
		print(random_response)
		print("I did not understand what you said so I am searching Wikipedia for you!")
		wikiprint = wikipedia.page(userInput)
		print (wikiprint.content)