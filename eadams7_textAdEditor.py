# Emily Adams
# Text Adventure Editor
# This program allows users to create and edit text-based adventure games. 

import json

def getMenuChoice():
    print(f"""
          0) exit
          1) load default game
          2) load a game file
          3) save the current file
          4) edit or add a node
          5) play the current game
          """)
    menuChoice = input("What will you do? ")
    return menuChoice

def main():
    defaultGame = getDefaultGame()
    keepGoing = True
    currentKey = "start"
    while keepGoing:
        menuChoice = getMenuChoice()
        if menuChoice == "0":
            keepGoing = False
        elif menuChoice == "1":
            defaultGame = getDefaultGame()
            print("Loaded default game")
        elif menuChoice == "2":
            loadGame()
        elif menuChoice == "3":
            saveGame()
        elif menuChoice == "4":
            editNode()
        elif menuChoice == "5":
            playGame()
        else:
            print(f"Invalid input.")

def getDefaultGame():
    defaultGame = {
        "start": ["Do you want to win or lose?", "I'm a winner!", "win", "I'm a big loser.", "lose"],
        "win": ["You win! I knew you could do it.", "Start over", "start", "Quit", "quit"],
        "lose": ["You lose! I'm so disappointed in you.", "Start over", "start", "Quit", "quit"]
    }
    return defaultGame

def playGame():
    defaultGame = getDefaultGame()
    currentKey = "start"
    keepGoing = True
    while keepGoing:
        if currentKey == "quit":
            keepGoing = False
        else:
            currentKey = playNode(defaultGame, currentKey)

def playNode(defaultGame, currentKey):
    currentNode = defaultGame[currentKey]
    (description, menuA, nodeA, menuB, nodeB) = currentNode
    print(f"""
          {description}
            1) {menuA}
            2) {menuB}
            """)
    choice = input("What will you do? ")
    if choice == "1":
        nextKey = nodeA
    if choice == "2":
        nextKey = nodeB
    else:
        nextKey == currentKey
    return nextKey

def saveGame():
    defaultGame = getDefaultGame()
    outFile = open("defaultGame.json", "w")
    json.dump(defaultGame, outFile, indent = 2)
    outFile.close 
    print(json.dumps(defaultGame, indent = 2))
    print("Saved defaultGame data to defaultGame.json")

def loadGame():
    inFile = open("defaultGame.json", "r")
    defaultGame = json.load(inFile)
    print(f"Game loaded successfully")
    return defaultGame
    
def editField(newNodeName):
    defaultGame = getDefaultGame()
    newNodeName = editNode()
    for currentValue in defaultGame:
        field = input(defaultGame[newNodeName])
        if field == "":
            currentValue = currentValue
        else:
            currentValue = open("defaultGame.json", "a")
            currentValue.write(newNodeName)
            json.dump(defaultGame, currentValue, indent=2)
            currentValue.close()
            print("saved defaultGame data to defaultGame.json")

def editNode():
    defaultGame = getDefaultGame()
    print(json.dumps(defaultGame, indent = 2))
    newNodeName = input("What node would you like to edit or create? ")
    if newNodeName in defaultGame.keys():
        newContent = defaultGame[newNodeName]
        (desc, menuA, nodeA, menuB, nodeB) = newContent
        newDesc = editField({desc})
        newMenuA = editField({menuA})
        newNodeA = editField({nodeA})
        newMenuB = editField({menuB})
        newNodeB = editField({nodeB})
        defaultGame[newNodeName] = [newDesc, newMenuA, newNodeA, newMenuB, newNodeB]
    else:
        newContent = ["","","","",""]
        (desc, menuA, nodeA, menuB, nodeB) = newContent
        newDesc = editField({desc})
        newMenuA = editField({menuA})
        newNodeA = editField({nodeA})
        newMenuB = editField({menuB})
        newNodeB = editField({nodeB})
        defaultGame[newNodeName] = [newDesc, newMenuA, newNodeA, newMenuB, newNodeB]
    return newNodeName

main()