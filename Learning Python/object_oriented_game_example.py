# Example of Python Classes

# We create a class called Player.

class Player:
    numberOfPlayers = 0
    playerList = []

    # This function (called a method in Object-Oriented Programming)
    # is called whenever a new object of Player is created.

    # It takes in one parameter, n, to set the name of the player.
    def __init__(self, n):
        Player.numberOfPlayers += 1 # This is now changed for the entire class
        self.name = n
        self.health = 100
        self.attack = 20
        self.level = 1
        self.items = ["Sword", "Health Potion"]

        Player.playerList.append(self)

    # Deal damage to the player. If the player is dead, report it.
    def takeDamage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print ("You have died!")
            Player.playerList.remove(self)

    # Level up the player. Does not take any other parameters.
    def levelUp(self):
        if self.level < 50:
            self.level += 1
            print ("Level up! You are now level " + str(self.level))
        else:
            print ("You are already max level!")


# Creating players
player1 = Player("John")
player2 = Player("Mike")

# Check how many players we now have, directly accessing the Class variable
print (Player.numberOfPlayers)

# This is the same for each object
print (Player.numberOfPlayers == player1.numberOfPlayers == player2.numberOfPlayers)

# If we change a class variable for a specific object, it desyncs it with
# from all other objects and the class.
player1.numberOfPlayers = 500
Player.numberOfPlayers = 20

print (Player.numberOfPlayers == player1.numberOfPlayers)
print (Player.numberOfPlayers == player2.numberOfPlayers)

# Deal damage to player 1
player1.takeDamage(50)

print (player1.health)
print (player2.health)

# PlayerList has 2 players in it
print (Player.playerList)

player1.takeDamage(100)

# PlayerList has 1 player in it
print (Player.playerList)
print(Player.items)