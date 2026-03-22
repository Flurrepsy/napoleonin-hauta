#Make deck of cards
#Suggestions on card differentiation system
#Naming convention example ace of spades is AS and 3 of diamonds is 3D
#System as list of 13 cards in 4 categories




#Build deck
def build_deck():

    aces = ['1S', 1],['2S', 2],['3S', 3],['4S', 4],['5S', 5],['6S', 6],['7S', 7],['8S', 8],['9S', 9],['10S', 10],['11S', 11],['12S', 12],['13S', 13]
    diamonds = ['1D', 1],['2D', 2],['3D', 3],['4D', 4],['5D', 5],['6D', 6],['7D', 7],['8D', 8],['9D', 9],['10D', 10],['11D', 11],['12D', 12],['13D', 13]
    clubs = ['1C', 1],['2C', 2],['3C', 3],['4C', 4],['5C', 5],['6C', 6],['7C', 7],['8C', 8],['9C', 9],['10C', 10],['11C', 11],['12C', 12],['13C', 13]
    hearts = ['1H', 1],['2H', 2],['3H', 3],['4H', 4],['5H', 5],['6H', 6],['7H', 7],['8H', 8],['9H', 9],['10H', 10],['11H', 11],['12H', 12],['13H', 13]

    deck = []
    deck.extend(aces)
    deck.extend(diamonds)
    deck.extend(clubs)
    deck.extend(hearts)
    return deck

deck = build_deck()


