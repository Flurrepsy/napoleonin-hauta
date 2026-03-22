a = []
print(a)

def asd():
	a.append(1)
	print(a)
	return
asd()
print(a)

'''
How to make the move legality checker

What needs to be done
	-Read the card number value
	-Compare card number value to card value in chosen space
	-Two space types: king and ace
	-Empty spaces need one legal move and a special case where the number is compared to the empty space value, currently 0
	-
	-Make functions kingchecker and acechecker
		-Called when the card slot is selected
		-Takes card(drawnCard) and chosen space type(spaceSelect) as input
		-Read the topmost card on space and compare drawnCard to it
		-If compatible, proceed with placing card
		-If incompatible, send error message and don't proceed
		-Feature to unselect card and change to discard function
DONE

How to complete playability

What needs to be done
	-When encountering illegal move, do not change the active card or delete from deck, discard piles, or sixes pile
		-Active card can be drawn, taken from discard pile, or from saved sixes
		DONE
	-Create win condition
		-All king's spaces need king
		AND
		-Ace pile needs four aces
	-Create fail condition
		-No more cards in deck
		AND
		-No more legal moves available from cards in discard pile and sixes pile
	-Move game "engine" logic into mainLoop.py

Making GUI

What needs to be done
	-Placeholder card images represent cards correctly
	-Make playing field
		-Slots for kings etc.
		-One slot for deck, clicking it will draw card
	-Make mouse clicks on cards, slots, deck represent actions
	-
Status of GUI 28.02
	-Pushbuttons represent card slots
		-Connect pushbuttons to play card function
			-When button is pressed,
		-Change label of pushbutton with card in slot
		-LATER resize pushbuttons and add card image to represent card in slot

	POSSIBLE BUGS
	When a card is drawn, there should be a system that handles the case where a discard space is clicked such that the drawn card does not disappear

Status on 02.03
	-Completely playable within GUI with primitive victory screen
	-Known issues
		-Pressing discard button multiple times discards the same card into multiple slots FIXED
		-Not much else at the moment
	-TO DO
		-Make discard mechanic better, not just clicking on the discard button
		-Make cards on field and on draw button have changing labels respective to card in slot
			-Eventually add card images as graphics DONE
		-Fix discard issue
		-Get better background image DONE
		-Make victory screen better DONE HALFWAY
Status on 04.03
	-GUI seems bug free, but the console throws up errors when doing some actions
	CORRECTION
	-A bug exists after clicking around on multiple slots randomly and ValueError appears in playCard(), not enough values to unpack (expected 3, got 2)
		-Makes placement of seemingly ONLY an ace into the king's slot has nothing to do with clicking the other slots
	-TO DO
		-Fix errors that appear in the console, that will probably help with some bugs.
		-Find out if pyinstaller works
		-GAMEPLAY IDEA maybe add function of moving cards from discard slots into empty slots

Status 07.03
	-Working exe for windows with no detected game crashing bugs
		-Tested only on my own windows

Status 12.03
	-Project finished
		-Some features that could be added if I'm arsed to ever revisit this one again
			-When deck is empty, ability to move cards from discard slots to other empty discard slots to subtly aid in game completion in cases of near misses
			-Basic control of card drawn from deck, click the card to select and double click for discard



'''



