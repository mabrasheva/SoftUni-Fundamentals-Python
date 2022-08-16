# A faro shuffle is a method for shuffling a deck of cards, in which the deck is split exactly in half.
# Then the cards in the two halves are perfectly interleaved, such that the original bottom card is still on the bottom
# and the original top card is still on top.
# For example, faro shuffling the list ['ace', 'two', 'three', 'four', 'five', 'six'] once,
# gives ['ace', 'four', 'two', 'five', 'three', 'six']
# Write a program that receives a single string (cards separated by space) and on the second line receives a count of
# faro shuffles that should be made. Print the state of the deck after the shuffle.
# Note: The length of the deck of cards will always be an even number.

deck_cards = input().split()
count_faro_shuffles = int(input())
temp_deck = deck_cards

middle = len(deck_cards) // 2
for shuffle in range(count_faro_shuffles):
    first_half = deck_cards[:middle]
    second_half = deck_cards[middle:]
    temp_deck = []
    for index in range(middle):
        temp_deck.append(first_half[index])
        temp_deck.append(second_half[index])
    deck_cards = temp_deck
print(deck_cards)
