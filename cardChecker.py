#
#Card checker that takes drawn card, selected space, and existing card in slot as inputs
def cardCheck(drawnCard, objectiveSpace, cardsInSlot):
	cardValue = int(drawnCard[1])
	selectedSpace = int(objectiveSpace)



	#Get value of card in slot
	#Compare played card to card in slot
	#King's spaces
	if selectedSpace == 1:
		slotCardValue = cardsInSlot[0][1]
		#Check for 7 into empty slot
		if slotCardValue == 0 and cardValue == 7:
			return True
		#Check if card in slot is ONE smaller than drawn card
		elif slotCardValue == (cardValue - 1) and cardValue != 1:
			return True
		else:
			return False

	elif selectedSpace == 3:
		slotCardValue = cardsInSlot[1][1]
		#Check for 7 into empty slot
		if slotCardValue == 0 and cardValue == 7:
			return True
		#Check if card in slot is ONE smaller than drawn card
		elif slotCardValue == (cardValue - 1) and cardValue != 1:
			return True
		else:
			return False

	elif selectedSpace == 7:
		slotCardValue = cardsInSlot[2][1]
		#Check for 7 into empty slot
		if slotCardValue == 0 and cardValue == 7:
			return True
		#Check if card in slot is ONE smaller than drawn card
		elif slotCardValue == (cardValue - 1) and cardValue != 1:
			return True
		else:
			return False
	elif selectedSpace == 9:
		slotCardValue = cardsInSlot[3][1]
		#Check for 7 into empty slot
		if slotCardValue == 0 and cardValue == 7:
			return True
		#Check if card in slot is ONE smaller than drawn card
		elif slotCardValue == (cardValue - 1) and cardValue != 1:
			return True
		else:
			return False
	#Space of Ace
	elif selectedSpace == 5:
		slotCardValue = cardsInSlot[4][1]
		#Check for 6 into empty slot or onto ace
		if (slotCardValue == 0 or slotCardValue == 1) and cardValue == 6:
			return True
		#Check if card in slot is ONE larger than drawn card
		elif slotCardValue == (cardValue + 1):
			return True
		else:
			return False

	#Save six space
	elif selectedSpace == 10:
		if cardValue == 6:
			return True
		else:
			#print("Can only play a six")
			return False
	else:
		#print("Not a valid space")
		return False

	return None


