import random
from enum import Enum


def find_approximate_value(value, percentRange):
    lowestValue = value - (percentRange / 100) * value
    highestValue = value + (percentRange / 100) * value
    return random.randint(lowestValue, highestValue)


Event = Enum('Event', ['Chest', 'Empty'])

eventDictionary = {Event.Chest: 0.6,
                   Event.Empty: 0.4
                   }

eventList = tuple(eventDictionary.keys())
eventprobability = tuple(eventDictionary.values())

Colours = Enum('Colours', {'Green': 'Green',
                           'Orange': 'Orange',
                           'Purple': 'Purple',
                           'Gold': 'Gold'
                           })

ChestColoursDictionary = {Colours.Green: 0.75,
                          Colours.Orange: 0.2,
                          Colours.Purple: 0.04,
                          Colours.Gold: 0.01,
                          }

ChestColourList = tuple(ChestColoursDictionary.keys())
ChestColourprobability = tuple(ChestColoursDictionary.values())

rewardForChests = {ChestColourList[reward]: (reward + 1)*(reward + 1) * 100
                   for reward in range(len(ChestColourList))
                   }


gameLength = 5
goldAcquired = 0

print("welcome in my game called KOMNATA")
print("""You have only 5 steps to make, see yourself
    how much gold You gonna acquired till the end""")

while gameLength > 0:
    gameAnswer = input("Do You want to move forward? ")
    if (gameAnswer == "yes"):
        print("Great let`s see what You got...")
        drawnEvent = random.choices(eventList, eventprobability)[0]
        if (drawnEvent == Event.Chest):
            print("You have drown a CHEST")
            drawnColour = random.choices(
                ChestColourList, ChestColourprobability)[0]
            print("the CHEST colour is...", drawnColour.value)
            gamerReward = find_approximate_value(
                rewardForChests[drawnColour], 10)
            goldAcquired = goldAcquired + gamerReward
        elif (drawnEvent == Event.Empty):
            print("You have drown nothing")
    else:
        print("You can go just straight")
        continue
    gameLength = gameLength - 1
print("Congratulations You have acquired: ", goldAcquired)
