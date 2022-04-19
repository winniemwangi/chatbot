print ("Hi! My name is Winnie, and I'm going to do some magic for you! But first, tell me a little bit about yourself.")
name = input (" Let's start with your name: ")
if (name == "Winnie"):
  print ("Yeppy! We have the same name!")

else:
  print ("Hi " + name + "!")
x=input ("What's your favorite thing to do? ")

print ("Wow, that's really cool! I wish I could do that! ")
siblings = input ("Do you have any siblings? ")
siblings = siblings.lower()
if (siblings == "yes"):
  numberSib = int(input ("Awesome! How many? "))
  if (numberSib >=4):
    print ("Woah, that's a lot of siblings! ")
  else:
    print ("Good to know! ")
  
elif (siblings == "no"):
  print ("An only child! I am too! ")
    
else:
  print ("Good to know! ")
  
      
      
      
print ("OK! Let's get started on some magic! ")
number1 = int(input ("Think of a number from 1 to 100. Once you have one, type it here: "))
input ("Ok, now multiply it by 5 (press enter to continue) ")
input ("Now divide it by 2 (Press enter to continue) ")
input ("Now add 10 (Press enter to continue) ")
input ("Is your number " + str(number1 * 5 / 2 + 10) + " ? ")
print ("See? MAGIC!")
print ("Let's try another one")
number2 = int (input ("Think of a number from 1-10. (Type 'enter' to continue)"))
input ( "Now mulitply by 4 (Press enter to continue")
input ( "Now divide by 2 (Press enter to continue) ")
input ( "Now multiply by 9 (Press enter to continue) ")
input ( "Is your number"  + str(number2 * 4 / 2 * 9) +  ("Press enter to continue") )

print ("Wow! you so amazing!", name, "That's it for my chatbot, thanks for visiting!")