#introduction

#----------------------------

name1 = input("Helllo, what is your name? ")

name1Cap = name1.capitalize()

print("Welcome " + name1Cap + "!")

coffee = input("Do you like coffee? Yes/No: ")

coffee1Low = coffee.lower()

if coffee1Low == ("no"):
    Favoritedrink = input("What is your favorite drink then? ")
    input("Why do you like " + (Favoritedrink) + "?")
else:
    input("What is your favorite coffee? ")

#icecream

#----------------------------

ice1 = input("What's your favorite ice cream? ")

ice1Cap = ice1.capitalize()

input((ice1Cap) + " is not a good ice cream. Please give good reason. ")

#math

#----------------------------

math1 = input("Here comes a math question. What is 4 + 4? ")


if int(math1) == 8:
    print("Well done.")
elif int(math1) <= 0:
    print("How bad can you be!?")
else:
    print("False. You really are bad at math :/")








