"""
This program takes a bridge hand and returns the optimal opening bid, using a simplified point-counting strategy to determine which opening bid would be best for the given hand.

Author: Chris Thomas
"""


import random

"""
This function returns a random bridge hand.
"""
def randomHand():
    deck = [] # list of all 52 possible cards, as 2-character strings
    for suit in "SHDC":
        for rank in "234567890JQKA":
            deck.append(rank+suit)

    random.shuffle(deck) # put deck in random order

    # take the first 13 cards from the shuffled deck
    handString = ""
    for i in range(13):
        handString += deck[i][0] + deck[i][1]

    return handString


"""
This function takes a bridge hand in string form as a parameter and returns an opening bid, also in string form.
"""
def bid(hand):
    if totalPoints(hand) < 14: # if the total points are less than 14, return "pass" as a string
        return "pass"
    else:
        if distPoints(hand) <= 1: # if the distribution points are less than or equal to 1, return "1 notrump" as a string
            return "1 notrump"
        else:
            cards = handToList(hand) # calls handToList function, passing hand as a string parameter
            count = suitCount(cards) # calls suitCount function, passing cards as a list parameter
            return whichBid(count)   # calls whichBid function, passing count as a list parameter, and returning the value of whichBid


"""
This function takes a bridge hand in string form as a parameter and returns the number of high-card points in the hand, as an integer.
"""
def highCardPoints(hand):
    cards = handToList(hand) # calls handToList function, passing hand as a string parameter
    hcPoints = 0
    i = 0
    while i < len(cards): # loops through each card in the hand, adding the appropriate number of high-card points to the total
        if cards[i][0] == "A":
            hcPoints+=4
        if cards[i][0] == "K":
            hcPoints+=3
        if cards[i][0] == "Q":
            hcPoints+=2
        if cards[i][0] == "J":
            hcPoints+=1
        i+=1
    return hcPoints # returns the number of high-card points


"""
This function takes a bridge hand in string form as a parameter and returns the number of distribution points in the hand, as an integer.
"""
def distPoints(hand):
    cards = handToList(hand)     # calls handToList function, passing hand as a string parameter
    cardCount = suitCount(cards) # calls cardCount function, passing cards as a list parameter
    dPoints = 0
    i = 0
    while i < len(cardCount): # loops through each value in cardCount, adding the appropriate number of distribution points to the total
        if cardCount[i] == 0:
            dPoints+=3
        if cardCount[i] == 1:
            dPoints+=2
        if cardCount[i] == 2:
            dPoints+=1
        i+=1
    return dPoints # returns the number of distribution points


"""
This function takes a bridge hand in string form as a parameter and returns the total number of points in the hand, as an integer.
"""
def totalPoints(hand):
    return highCardPoints(hand) + distPoints(hand) # calls highCardPoints and distPoints functions, passing hand as a string parameter to both, and returning the value of their sum


"""
This function takes a bridge hand in the form of a list of cards as a parameter and returns the number of cards each suit has in the hand, as a list.
"""
def suitCount(cards):
    i = 0
    suitCount = [0, 0, 0, 0]
    while i < len(cards): # loops through each card in the hand, incrementing the corresponding suit's counter
        if cards[i][1] == "S":
            suitCount[0]+=1
        else:
            if cards[i][1] == "H":
                suitCount[1]+=1
            else:
                if cards[i][1] == "D":
                    suitCount[2]+=1
                else:
                    suitCount[3]+=1
        i+=1
    return suitCount # returns each the total number of cards of each suit in the hand


"""
This function takes the number of cards of each suit in the player's hand as a list and returns the bid they should make as a string.
"""
def whichBid(suitCount):
    if suitCount[0] >= suitCount[1] and suitCount[0] >= suitCount[2] and suitCount[0] >= suitCount[3]: # if there are as many or more spades in the hand than any other suit, return "1 spade" as a string
        return "1 spade"
    else:
        if suitCount[1] >= suitCount[2] and suitCount[1] >= suitCount[3]: # if there are as many or more hearts in the hand than either diamonds or clubs, return "1 heart" as a string
            return "1 heart"
        else:
            if suitCount[2] >= suitCount[3]: # if there are as many or more diamonds in the hand than clubs, return "1 diamond" as a string
                return "1 diamond"
            else: # there are more clubs in the hand than any other suit, return "1 club" as a string
                return "1 club"


"""
This function takes a bridge hand in string form and returns the same hand, as a list of the cards it contains.
"""
def handToList(hand):
    cards = []
    i = 0
    while i < len(hand)-1:# loops through every other value in the string and appends the number-letter representation of a card to the list of cards
        cards.append(hand[i] + hand[i+1])
        i+=2
    return cards # returns the list of cards


"""
Some example hands:
"""
# 3 high card points, 1 distribution point, total 4, bid = pass
hand1 = '7CJH9H5H7S2DJS5C8C4DJD6H2H'

# 11 high card points, 2 distribution point, total 13, bid = pass
hand2 = 'QD4S3H6D4HKS8C7SACQH7H2H0S'

# 13 high card points, 1 distribution point, total 14, bid = notrump
hand3 = 'ADQS4C3DJH9S3CQD3S7S5HKHJD'

# 15 high card points, zero distribution points, total 15, bid = notrump
hand4 = '4HADKC6HASQS8DQC6S9H8C6D0D'

# 12 high card points, 3 distribution points, total 15, bid = 1 spade
hand5 = '4SASJSJC2C9HAD0DQS3S7D5S4D'

# 17 high card points, 2 distribution points, total 19, bid = 1 heart
hand6 = 'KH6S8H0HJCKD4HASAD5HQS7H6C'

# 11 high card points, 3 distribution points, total 14, bid = 1 club
hand7 = '2D6DJS3S0C6CJDKC4CAS3DQC2S'

# 10 high card points, 5 distribution points, total 15, bid = 1 diamond
hand8 = '2CQC5DKC7C9CKD6DJDJC8S0D3D'
