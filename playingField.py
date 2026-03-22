#Playing field
import importlib
import shuffleDeck as sh
import draw_card as drwcrd
import cardChecker as cc

importlib.reload(cc)
importlib.reload(drwcrd)

#Four objective spaces which allow 7->King incrementally
#One space in the middle which allows 6 -> Ace incrementally
#Four spaces for discard, from which cards can be played onto objective spaces

objectiveSpaceK1 = [['null', 0]]
objectiveSpaceK2 = [['null', 0]]
objectiveSpaceK3 = [['null', 0]]
objectiveSpaceK4 = [['null', 0]]
objectiveSpaceAce = [['null', 0]]
discardSpace1 = [['null', 0]]
discardSpace2 = [['null', 0]]
discardSpace3 = [['null', 0]]
discardSpace4 = [['null', 0]]
storeSix = [['null', 0]]

def resetField():
    #Represent playing field spaces as lists
    for i in range(len(objectiveSpaceK1)-1):
        objectiveSpaceK1.pop(0)
    for i in range(len(objectiveSpaceK2)-1):
        objectiveSpaceK2.pop(0)
    for i in range(len(objectiveSpaceK3)-1):
        objectiveSpaceK3.pop(0)
    for i in range(len(objectiveSpaceK4)-1):
        objectiveSpaceK4.pop(0)
    for i in range(len(objectiveSpaceAce)-1):
        objectiveSpaceAce.pop(0)
    for i in range(len(discardSpace1)-1):
        discardSpace1.pop(0)
    for i in range(len(discardSpace2)-1):
        discardSpace2.pop(0)
    for i in range(len(discardSpace3)-1):
        discardSpace3.pop(0)
    for i in range(len(discardSpace4)-1):
        discardSpace4.pop(0)
    for i in range(len(storeSix)-1):
        storeSix.pop(0)
    return



#Primitive visual playing field
def renderField():
    print("({})    ({})    ({})".format(objectiveSpaceK3[0], discardSpace1[0], objectiveSpaceK4[0]))
    print("({})    ({})    ({})".format(discardSpace4[0], objectiveSpaceAce[0], discardSpace2[0]))
    print("({})    ({})    ({})".format(objectiveSpaceK1[0], discardSpace3[0], objectiveSpaceK2[0]))
    print("")
    print("({})".format(storeSix[0]))
    print("")
    return




#Play a card
def playCard(drawnCard, turnCounter, chosenSpace, shuffledDeck, discarded, discardedFrom):
    fieldCards = [objectiveSpaceK1[0], objectiveSpaceK2[0], objectiveSpaceK3[0], objectiveSpaceK4[0], objectiveSpaceAce[0]]
    #spaceSelect = input("Choose where to play 1, 3, 7, 9, dis, or save 6 with s: ")
    spaceSelect = chosenSpace
    #print(spaceSelect)
    #print("Cards remaining in deck: {}".format(len(shuffledDeck)))
    #Try except else for integer or string inputs
    try:
        int(spaceSelect)

    except ValueError:
        #Storing of sixes
        if spaceSelect == "disc" and drawnCard[1] == 6:
            #Change to int to avoid ValueErrors in cardChecker
            spaceSelect = 10
            cardOk = cc.cardCheck(drawnCard, spaceSelect, fieldCards)
            if cardOk == True:
                storeSix.insert(0, drawnCard)
                del shuffledDeck[0]
        #Discard
        elif spaceSelect == "disc" and drawnCard != ("null", 0):
            #Tick turncounter here to only count discards
            cardOk = True
            turnCounter = turnCounter + 1
            if turnCounter == 1 and len(shuffledDeck) != 0:
                discardSpace1.insert(0, drawnCard)
                drawnCard = 0, 0
                del shuffledDeck[0]
            elif turnCounter == 2 and len(shuffledDeck) != 0:
                discardSpace2.insert(0, drawnCard)
                drawnCard = 0, 0
                del shuffledDeck[0]
            elif turnCounter == 3 and len(shuffledDeck) != 0:
                discardSpace3.insert(0, drawnCard)
                drawnCard = 0, 0
                del shuffledDeck[0]
            elif turnCounter == 4 and len(shuffledDeck) != 0:
                discardSpace4.insert(0, drawnCard)
                drawnCard = 0, 0
                del shuffledDeck[0]
        elif drawnCard == 0:
            return turnCounter, cardOk, drawnCard
        else:
            cardOk = False
            return turnCounter, cardOk, drawnCard
    else:
        #Play to objective space
        #First run card checker, spaceSelect for selecting space and determining the objectiveSpace number


        #Run cardchecker, return true or false for move validity
        #print(fieldCards)
        cardOk = cc.cardCheck(drawnCard, spaceSelect, fieldCards)
        #print(discarded)
        #print(discardedFrom)
        #If valid move, play card to selected space
        #King spaces
        if discarded == False:
            if int(spaceSelect) == 1 and cardOk == True:
                objectiveSpaceK1.insert(0, drawnCard)
                del shuffledDeck[0]
            elif int(spaceSelect) == 3 and cardOk == True:
                objectiveSpaceK2.insert(0, drawnCard)
                del shuffledDeck[0]
            elif int(spaceSelect) == 7 and cardOk == True:
                objectiveSpaceK3.insert(0, drawnCard)
                del shuffledDeck[0]
            elif int(spaceSelect) == 9 and cardOk == True:
                objectiveSpaceK4.insert(0, drawnCard)
                del shuffledDeck[0]
            #Space of Ace
            elif int(spaceSelect) == 5 and cardOk == True:
                objectiveSpaceAce.insert(0, drawnCard)
                del shuffledDeck[0]
            else:
                #print("Cannot insert card")
                return turnCounter, cardOk, drawnCard

        elif discarded == True:
            if int(spaceSelect) == 1 and cardOk == True:
                objectiveSpaceK1.insert(0, drawnCard)

            elif int(spaceSelect) == 3 and cardOk == True:
                objectiveSpaceK2.insert(0, drawnCard)

            elif int(spaceSelect) == 7 and cardOk == True:
                objectiveSpaceK3.insert(0, drawnCard)

            elif int(spaceSelect) == 9 and cardOk == True:
                objectiveSpaceK4.insert(0, drawnCard)

            #Space of Ace
            elif int(spaceSelect) == 5 and cardOk == True:
                objectiveSpaceAce.insert(0, drawnCard)

            else:
                #print("Cannot insert card")
                return turnCounter, cardOk, drawnCard
        if discardedFrom == "d1" and discarded == True:
            discardSpace1.pop(0)
            turnCounter = 0
        elif discardedFrom == "d2" and discarded == True:
            discardSpace2.pop(0)
            turnCounter = 1
        elif discardedFrom == "d3" and discarded == True:
            discardSpace3.pop(0)
            turnCounter = 2
        elif discardedFrom == "d4" and discarded == True:
            discardSpace4.pop(0)
            turnCounter = 3
        elif discardedFrom == "six" and discarded == True:
            storeSix.pop(0)




    if turnCounter == 4:
        turnCounter = 0
    if cardOk == True:
        drawnCard = "null", 0
    return turnCounter, cardOk, drawnCard


gameState = 0
turnCounter = 0

#while gameState == 0:
   # gameState = input("Press any key to start: ")
    #shuffled_deck = sh.shuffle_deck()


def actionSelect(turnCounter, shuffled_deck, drawnCard, actSelect):
    #Choose draw or play from discard or sixes pile

    #actSelect = input("Choose d for draw, p to play from discard, six to play stored 6: ")
    actSelect = actSelect
    discarded = True
    if actSelect == "draw":
        drawnCard = drawnCard
        #print("here")
        #Check for empty deck
        if drawnCard != 0:

            turnCounter, cardOk = playCard(drawnCard, turnCounter, actSelect)
        else:
            return turnCounter

        if cardOk == True:
            del shuffled_deck[0]
            #print("Cards remaining in deck: {}".format(len(shuffled_deck)))
            #print("")
        if turnCounter == 4:
            turnCounter = 0

    #System to choose which discard pile to play from and check card legality for removal of car from pile
    # #elif actSelect == "p":
        #discardSelect = input("Choose discard pile to draw from: ")
    elif actSelect == "d1":
        #discardSelect = int(discardSelect)
        #turnCounter = 0
        drawnCard = discardSpace1[0]
        #turnCounter, cardOk = playCard(drawnCard, turnCounter, actSelect, shuffled_deck)
        #if cardOk == True:
           # discardSpace1.pop(0)
    elif actSelect == "d2":
        #discardSelect = int(discardSelect)
        #turnCounter = 1
        drawnCard = discardSpace2[0]
        #turnCounter, cardOk = playCard(drawnCard, turnCounter, actSelect, shuffled_deck)
        #if cardOk == True:
            #discardSpace2.pop(0)
    elif actSelect == "d3":
        #discardSelect = int(discardSelect)
        #turnCounter = 2
        drawnCard = discardSpace3[0]
        #turnCounter, cardOk = playCard(drawnCard, turnCounter, actSelect, shuffled_deck)
        #if cardOk == True:
            #discardSpace3.pop(0)
    elif actSelect == "d4":
        #discardSelect = int(discardSelect)
        #turnCounter = 3
        drawnCard = discardSpace4[0]
        #turnCounter, cardOk = playCard(drawnCard, turnCounter, actSelect, shuffled_deck)
        #if cardOk == True:
            #discardSpace4.pop(0)

    #System to play from sixes pile
    elif actSelect == "six":
        drawnCard = storeSix[0]
        #turnCounter, cardOk = playCard(drawnCard, turnCounter, actSelect)
        #if cardOk == True:
                #storeSix.pop(0)
    else:
        cardOk = False
        return turnCounter, cardOk
    #renderField()
    discardedFrom = actSelect
    return turnCounter, drawnCard, discarded, discardedFrom


def victoryCondition():
    if (
        len(objectiveSpaceK1) == 8
        and len(objectiveSpaceK2) == 8
        and len(objectiveSpaceK3) == 8
        and len(objectiveSpaceK4) == 8
        and len(objectiveSpaceAce) == 25
        and objectiveSpaceAce[0][0] in ("1S", "1D", "1H")):
        return True
    elif (
        len(objectiveSpaceK1) == 8
        and len(objectiveSpaceK2) == 8
        and len(objectiveSpaceK3) == 8
        and len(objectiveSpaceK4) == 8
        and len(objectiveSpaceAce) == 25
        and objectiveSpaceAce[0][0] == "1C"):
        return "totalVictory"
    else:
        return False











