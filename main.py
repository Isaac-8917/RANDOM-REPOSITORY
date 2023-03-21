print("Info: when text stops appearing type Space then Enter to Continue. You are reminded the first time.")
userName = input("Hello user! What is your name? (Dont put a space)")
userConfirmation = print(f"Hello, Private {userName}!")

print("Welcome to the Army Academy!")
print("Space then Enter to Continue")
Continue = input("> ")
if(Continue == " "):
  print("Your goal is to climb the ranks of the Army.") 
  print("Do you want to start your training?")
  trainingChoice1 = input("> ")
  if (trainingChoice1 == "yes"):
    print("Great! Lets begin!")
    Continue = input("> ")
    if(Continue == " "):
      print("We will start with a physical exam.")
  elif (trainingChoice1 == "no"):
      print("You are removed from the Academy.")
      exit()

  else:
    print("Invalid answer. Please respond with yes or no. ")
    exit()
