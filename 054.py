#!/usr/bin/python
# -*- coding: utf-8 -*-

#In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

    #* High Card: Highest value card.
    #* One Pair: Two cards of the same value.
    #* Two Pairs: Two different pairs.
    #* Three of a Kind: Three cards of the same value.
    #* Straight: All cards are consecutive values.
    #* Flush: All cards of the same suit.
    #* Full House: Three of a kind and a pair.
    #* Four of a Kind: Four cards of the same value.
    #* Straight Flush: All cards are consecutive values of same suit.
    #* Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

#The cards are valued in the order:
#2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

#If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

#Consider the following five hands dealt to two players:
#Hand	 	Player 1	 	Player 2	 	Winner
#1	 	5H 5C 6S 7S KD
#Pair of Fives
	 	#2C 3S 8S 8D TD
#Pair of Eights
	 	#Player 2
#2	 	5D 8C 9S JS AC
#Highest card Ace
	 	#2C 5C 7D 8S QH
#Highest card Queen
	 	#Player 1
#3	 	2D 9C AS AH AC
#Three Aces
	 	#3D 6D 7D TD QD
#Flush with Diamonds
	 	#Player 2
#4	 	4D 6S 9H QH QC
#Pair of Queens
#Highest card Nine
	 	#3D 6D 7H QD QS
#Pair of Queens
#Highest card Seven
	 	#Player 1
#5	 	2H 2D 4C 4D 4S
#Full House
#With Three Fours
	 	#3C 3D 3S 9S 9D
#Full House
#with Three Threes
	 	#Player 1

#The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

#How many hands does Player 1 win?

#Answer:
	#376

from time import time; t=time()

CARD = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
for i in range(2, 10):
    CARD[str(i)] = i

def game(org_cards1, org_cards2):
    cards1 = list(map(lambda s:(CARD[s[0]], s[1]), org_cards1))
    cards2 = list(map(lambda s:(CARD[s[0]], s[1]), org_cards2))
    rank1 = get_rank(cards1)
    rank2 = get_rank(cards2)
    assert rank1 != rank2
    if rank1 > rank2: return 1
    return 2

def get_rank(cards):
    assert len(cards) == 5
    nums, suits = zip(*sorted(cards))
    suitcnt = len(set(suits))
    numcnt = len(set(nums))
    is_consec = all(nums[i]-nums[0] == i for i in range(5))
    if suitcnt == 1 and is_consec:
        # Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
        if nums[0] == 10: return 9
        # Straight Flush: All cards are consecutive values of same suit.
        return 8, nums[4]
    if numcnt == 2:
        # Four of a Kind: Four cards of the same value.
        if nums[0] == nums[3]: return 7, nums[0], nums[4]
        if nums[1] == nums[4]: return 7, nums[1], nums[0]
        # Full House: Three of a kind and a pair.
        if nums[0] == nums[2]: return 6, nums[0], nums[3]
        if nums[1] == nums[3]: return 6, nums[1], nums[0]
        if nums[2] == nums[4]: return 6, nums[2], nums[0]
        1/0
    # Flush: All cards of the same suit.
    if suitcnt == 1: return 5, nums[4], nums[3], nums[2], nums[1], nums[0]
    # Straight: All cards are consecutive values.
    if is_consec: return 4, nums[4]
    # Three of a Kind: Three cards of the same value.
    if nums[0] == nums[2]: return 3, nums[2], nums[4], nums[3]
    if nums[1] == nums[3]: return 3, nums[3], nums[4], nums[0]
    if nums[2] == nums[4]: return 3, nums[4], nums[1], nums[0]
    if numcnt == 3:
        # Two Pairs: Two different pairs.
        if nums[3] != nums[4]: return 2, nums[3], nums[1], nums[4]
        if nums[2] != nums[1]: return 2, nums[4], nums[1], nums[2]
        if nums[1] != nums[0]: return 2, nums[4], nums[2], nums[0]
        1/0
    if numcnt == 4:
        # One Pair: Two cards of the same value.
        for i in range(4):
            if nums[i] == nums[i+1]:
                s = nums[i]
                nums = sorted(list(nums))[::-1]
                nums.remove(s)
                nums.remove(s)
                return (1, s) + tuple(nums)
    assert numcnt == 5
    # High Card: Highest value card.
    return 0, nums[4], nums[3], nums[2], nums[1], nums[0]

cnt = 0
for l in open('054-poker.txt').read().splitlines():
    allcards = l.split()
    if game(allcards[:5], allcards[5:]) == 1: cnt += 1

print(cnt)#, time()-t
