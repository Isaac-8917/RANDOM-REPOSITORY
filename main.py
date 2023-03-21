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
    if (Continue == " "):
      print("We will start with a physical exam.")
      print("You will have to complete 10 JJ's")
      print("You will do them like ONE. TWO. Ect.")
      Continue == input ("> ")
      if (Continue == " "):
        print("Start")
        JJ = input("> ")
        if (JJ == "ONE."):
          print("Good! Again!")

        else:
          print("You Failed!")
          exit()
          if (JJ == "TWO."):
            print("Good! Again!")
          else:
            print("You Failed!")
            exit()
          if (JJ == "THREE."):
            print("Good! Again!")
          else:
            print("You Failed!")
            exit()
          if (JJ == "FOUR."):
            print("Good! Again!")
          else:
            print("You Failed!")
            exit()
          if (JJ == "FIVE."):
            print("Good! Again!")
          else:
            print("You Failed!")
            exit()
          if (JJ == "SIX."):
            print("Good! Again!")
          else:
            print("You Failed!")
            exit()
          if (JJ == "SEVEN."):
            print("Good! Again!")
          else:
            print("You Failed!")
            exit()
          if (JJ == "EIGHT."):
            print("Good! Again!")
          else:
            print("You Failed!")
            exit()
          
          if (JJ == "NINE."):
            print("Good! Again!")
          else:
            print("You Failed!")
            exit()
          if (JJ == "TEN!."):
            print("Good Job1 We will test you now!")
          else:
            print("You Failed!")
            exit()
          
          

        
        
  elif (trainingChoice1 == "no"):
      print("You are removed from the Academy.")
      exit()

  else:
    print("Invalid answer. Please respond with yes or no. ")
    exit()
