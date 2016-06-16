import random
from Player import *
from Dealer import *
from GameFlow import *
from Ui import *

class Deck(object):

	def __init__(self):
		self.deck = []
		self.suits = ['spades','clubs','diamonds','hearts']
		self.new_deck = ''


	def createdeck(self):
		'''
		Creats a new set of 52 cards and shuffles the deck
		:return: list of 52 tuples representing each card (nomination, card suit, point value)
		'''

		for cards in range(2,11):
			for i in self.suits:
				self.deck.append((str(cards), i, cards))
		for c in ['jack', 'quin', 'king', 'ace']:
			for i in self.suits:
				if c == 'ace':
					self.deck.append((c, i, 11))
				else:
					self.deck.append((c, i, 10))
		random.shuffle(self.deck)




	def dealhand(self):
		'''
		Takes top card and removes it from the deck, if deck is less than 10 cards, create and shuffle new deck
		:return: top card in the form of tuple (nomination, card suit, point value)
		'''
		self.new_deck = ''
		card = self.deck.pop(0)
		if len(self.deck) < 10:
			self.createdeck()
			self.new_deck = 'New deck!'
		return card











