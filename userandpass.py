username = 'root'

password = 'root'
n = 5
while n > 3:
   userInput = input("What is your username?\n")

   if userInput == username:
      userInput = input("Password?\n")   
      if userInput == password:
         print("Welcome!")
         n = 2
      else:
         print("That is the wrong password.")
   else:
      print("That is the wrong username.")