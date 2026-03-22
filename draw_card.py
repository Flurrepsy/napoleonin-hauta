import shuffleDeck as shf

#deck = shf.build_deck()
#shuffled_deck = shf.shuffle_deck(deck)

#Draw a card from the deck
#First index is top card in deck
#Pick index 0, display card, delete card from deck
def draw_card(shuffled_deck):

    try:
        drawnCard = shuffled_deck[0]
    except IndexError:
        #print("")
        #print("There are no more cards in the deck.")
        #print("")
        #Make a card identifier that signifies the empty deck
        drawnCard = ["null", 0]
    #else:
        #print(shuffled_deck[0])
    #del shuffled_deck[0]
    return drawnCard

