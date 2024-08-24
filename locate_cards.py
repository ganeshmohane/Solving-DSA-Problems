
# Find the Card Problem

# Its Card Game, so there are multiple cards are given
# u have to choose or pick up the told one card and you should pick up in few tries 
# for example cards = [2,4,6,8,9] now u have to pick 8 but u dont know where it is as it is 
# upside down so u have to use see & try and find that cards position

#I have added if there are multiple no. still we my code will work and return there indexes

cards = [34,2,5,67,6,0,67]
find_card = 67
def locate_card(cards,find_card):
    position = 0
    same_cards = []
    while position < len(cards):
        if cards[position] == find_card:
            same_cards.append(position)
        position += 1
    return same_cards

result = locate_card(cards,find_card)
print(result)