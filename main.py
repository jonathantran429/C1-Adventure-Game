import random

print("Welcome to Jonathan's adventure game! In this game, you must escape a bear running after you in a misty forest. \n\nYou must keep track of your thirst, injuries, and more. Keep your thirst and injury levels low, while keeping your energy high.\n\nThere is a village a few hundred meters in front of you!\n\nBe careful out there!")

choice = 0
injuryLevel = 3
thirstLevel = 0
waterSupply = 5
distanceTraveled = 40
enemyDistance = 80
energyLevel = 20
werewolves = random.randint(1,10000)

while (choice != "g" and thirstLevel < 10 and injuryLevel < 15 and energyLevel > 3 and enemyDistance > 1 and distanceTraveled < 200):

  if (energyLevel <= 5):
    print("\nWarning; you are getting tired!")
  if(injuryLevel >= 10):
    print("\nWarning; your injuries are starting to create great blood loss!")
  if(thirstLevel >= 6):
    print ("\nWarning; you are getting thirsty!")
  if(waterSupply <= 2):
    print ("\nWarning; your canteen is getting empty!")

  choice = input("\nYou have 7 options to choose from. Use your intuition:\n\nA) Find Water\nB) Drink Water\nC) Apply Bandages\nD) Settle Down\nE) Run\nF) Status Check\nG) Quit\n\nWhat do you choose: ").lower()

  cottage = random.randint(0, 10)

  if (choice == "a"):
    findWater = random.randint(0, 10)
    if (findWater < 8):
      injuryLevel += 2
      energyLevel -= 1
      thirstLevel = 0
      waterSupply = 5
      enemyDistance -= random.randint(15,30)
      print ("\nYou set out to find water, and come across a small stream of crystal clear water. \nYou drink up and fill your canteen if it isn't already full along the way. \nYour thirst is gone, but you know that it's time to move.")
    else:
      injuryLevel += 2
      energyLevel -= 1
      enemyDistance -= random.randint(15,30)
      print("\nUnfortunately, you cannot find a stream and you know it is time to get moving.")
  elif (choice == "b"):
    thirstLevel = 0
    energyLevel += 2
    waterSupply -= random.randint(1,2)
    print ("\nQuickly, you pull out your canteen and gulp down a large portion of water. \nYou feel rejuvinated.")
  elif (choice == "c"):
    injuryLevel -= 5
    enemyDistance -= random.randint(10,20)
    print ("\nAfter applying bandages, you start to feel less blood seeping out of your cut. \nThe injury is sealed for now.")
  elif (choice == "d"):
    energyLevel += 10
    enemyDistance -= 6
    waterSupply -= 0.7
    thirstLevel -= 7
    print ("\nAfter a little stop at a clearing between a few trees, you feel energized and ready to keep moving.")
  elif (choice == "e"):
    if (cottage != 0):
      energyLevel -= 3
      enemyDistance += random.randint(25,45)
      distanceTraveled += 20
      thirstLevel += random.randint(1,3)
      injuryLevel += 1
      print("\nDue to your injuries, you cannot run far, but you do manage to hobble farther towards a distant clearing. ")
    else:
      thirstLevel = 0
      waterSupply = 5
      distanceTraveled += 16
      enemyDistance -= 10
      print("\nAfter traveling a small distance, you come across a cozy, brick cottage! Your thirst is eliminated and you fill your canteen.")
  elif (choice == "f"):
    print ("\nYou have " + str(waterSupply) +"/5 of your canteen filled.\nYour energy level is: " + str(energyLevel) + "\nYour injury level is: " + str(injuryLevel) + "\nYour thirst level is: " + str(thirstLevel) + "\nThe bear is " + str(enemyDistance) + " meters behind you" + "\nYou are " + str(400-distanceTraveled) + " meters from a village in which you can settle")
  elif (choice == "g"):
    choice = "g"
  else:
    print ("Invalid Input.")


if (choice == "g"):
  print("\nYou quit. Game Ended")
elif (thirstLevel >= 10):
  print("\nHowever, you have died of thirst. Game Ended")
elif (injuryLevel >= 15):
  print("\nHowever, your injuries have gotten too severe, and you have bled out. Game Ended")
elif (energyLevel < 3):
  print("\nHowever, you are so exhausted, you can't help but drift into a deep sleep. There, other animals find you and tear you up. Game Ended")
elif (enemyDistance < 1):
  print("\nHowever, you have spent too much time tending to your problems, that, unfortunately, the bear caught up. Game Ended")
elif (distanceTraveled >= 50):
  if (werewolves == 1):
    print("\nUnfortunately, you died to a werewolf as you made it to the village.")
  else:
    print("\nCongrats! You made it to the village and won!")
