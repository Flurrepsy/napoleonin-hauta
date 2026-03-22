import importlib
import shuffleDeck as sh
import draw_card as drwcrd
import cardChecker as cc
import playingFieldLegacy as pf

importlib.reload(cc)
importlib.reload(drwcrd)
importlib.reload(pf)
importlib.reload(sh)
#Main game loop
gameState = 0
turnCounter = 0



while 1:
    while gameState == 0:
        gameState = input("Press any key to start: ")


    #Generate playing field
    pf.resetField()
    pf.renderField()

#Generate shuffled deck
    shuffled_deck = sh.shuffle_deck()
    #print(shuffled_deck)
#Loop the drawing card thing through the entire deck
    while len(shuffled_deck) != 0:
        turnCounter = pf.actionSelect(turnCounter, shuffled_deck)
        pf.renderField()

#When all cards are drawn
    while not shuffled_deck:
        pf.actionSelect(1, 2)
        pf.renderField()
        quitPrompt = input("Press q to end round, a to continue: ")
        if quitPrompt == "q":
            break
#Game is over, either win or loss, restart or quit
    vc = pf.victoryCondition()
    if vc == True:
        print("Victory!")
    #IMPORTANT make condition in corner case where deck has run out but legal moves still exist
    restartChoice = input("Restart? y/n: ")
    if restartChoice == "y":
        gameState = 0
        turnCounter = 0
    else:
        break
    #turnCounter = 0
