import random

#Enter the minimum and maximum limits of the dice rolls below

min= 1

max = 6

#the variable that stores the user’s decision

Roll_Again = "yes"

#The dice roll loop if the user wants to continue

while Roll_Again == "yes" or Roll_Again == "y":

    print("Dices rolling<> <> <>")

    print("The values are :")

#Printing the randomly generated variable of the first dice

    print(random.randint(min, max))

#Printing the randomly generated variable of the second dice

    print(random.randint(min,max))

#Here the user enters yes or y to continue and any other input ends the program

    Roll_Again = input("Roll the Dices Again?\n")
