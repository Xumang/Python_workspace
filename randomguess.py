
import random

def main():
	print ("Guess any number between 1 and 100.")
	randomNumber = random.randint(1,100)
	found = False

	while not found:
		userGuess = int(input("Your Guess:"))
		if userGuess == randomNumber:
			print ("That's TRUE. YOU ARE GREAT")
			found = True 
		elif userGuess > randomNumber:
			print ("Guess the lower value:")
		else:
			print("Guess the higher value:")

	

main()

if __name__ == "__main__":
	print ('hello world')
	main()
