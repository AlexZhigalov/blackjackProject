from Deck import *
from Ui import *
from Player import *
from GameFlow import *

class Dealer(object):

	def __init__(self):
		self.count = 0
		self.winner = ''
		self.trackAces = []
		self.hide_first_card = False
		self.first_card = []
		self.count_to_display = 0

	def dealer_to_bet(self):
		if self.count <= 17 and self.winner == '':
			return True
		else:
			return False

	def dealer_to_bet_if_player_stays(self, player_stay, player):
		if player_stay and player.count > self.count and self.count < 21:
			return True
		return False

	def first_card_display(self, game):
		if self.hide_first_card == True and game.round == True:
			self.first_card.append(game.dealer_hand[0])
			game.dealer_hand[0] = ('','')
		else:
			if self.hide_first_card == True and not game.round and game.first_hand:
				pass
			else:
				game.dealer_hand[0] = self.first_card[0]


	def points_to_display(self,game, player):
		if player.stay == False and game.round:
			if len(game.dealer_hand) <= 1:
				return self.count
			return game.dealer_hand[1][2]

		else:
			return self.count




