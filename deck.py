#Make deck of cards
#Suggestions on card differentiation system
#Naming convention example ace of spades is AS and 3 of diamonds is 3D
#System as list of 13 cards in 4 categories

aces = ["1S", "2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "10S", "11S", "12S", "13S"]
diamonds = ["1D", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "11D", "12D", "13D"]
clubs = ["1C", "2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "10C", "11C", "12C", "13C"]
hearts = ["1H", "2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "10H", "11H", "12H", "13H"]

#Build deck
def build_deck():
    deck = []
    deck.append(aces)
    deck.append(diamonds)
    deck.append(clubs)
    deck.append(hearts)

    return deck

deck = build_deck()
