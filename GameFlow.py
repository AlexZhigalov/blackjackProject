from Dealer import *
from Player import *
from Deck import *
from Ui import *
import os


class GameFlow(object):
	max = 21

	def __init__(self):
		self.player_hand = []
		self.dealer_hand = []
		self.round = True
		self.first_hand = True


	def check_busted(self, player, dealer):
		if player.count > 21 or dealer.count > 21:
			if player.count > 21:
				player.winner = player.name +' busted!'
			if dealer.count > 21:
				dealer.winner = 'Dealer busted!'

	def check_winner(self,player, dealer):
		if self.first_hand:
			if player.count == self.max or dealer.count == self.max:
				if player.count == self.max:
					player.winner = player.name + ' wins!'
				if dealer.count == self.max:
					dealer.winner = 'Dealer wins!'
				#dealer.first_card_display(False, game)
				#dealer.points_to_display(game)


	def check_winner_when_stay(self, player, dealer):
		if player.stay and not dealer.dealer_to_bet():
			if player.count == dealer.count:
				player.winner = player.name + " wins!"
				dealer.winner = 'Dealer wins!'
			elif player.count > dealer.count:
				player.winner = player.name + ' wins!'
			else:
				dealer.winner = 'Dealer wins!'

	def end_round(self, player, dealer):
		self.round = False
		if player.winner == player.name + ' wins!':
			player.bank_add()
			player.trackAces = []
		elif dealer.winner == 'Dealer wins!':
			dealer.trackAces = []
		else:
			player.bank += player.bet




	def round_reset(self,player, dealer):
		player.count = 0
		player.trackAces = []
		player.bet_accepted = ''
		player.bet = 0
		player.stay = False
		player.winner = ''
		self.round = True
		self.dealer_hand = []
		self.player_hand = []
		self.first_hand = True
		dealer.winner = ''
		dealer.count = 0
		dealer.trackAces = []
		dealer.count_to_display = 0
		dealer.first_card = []
		dealer.hide_first_card = True

	def check_points(self, player, dealer):
		#check players current points
		self.check_winner_when_stay(player, dealer)
		self.check_winner(player, dealer)
		self.check_busted(player, dealer)

		if player.winner != '' and dealer.winner != '' and player.winner[-2] == dealer.winner[-2] == 'd':
			player.winner += ' PUSH'
			dealer.winner += ' PUSH'
			self.end_round(player, dealer)

		elif player.winner != '' and dealer.winner != '' and player.winner[-2] == dealer.winner[-2] == 's':
			player.winner += ' PUSH'
			dealer.winner += ' PUSH'
			self.end_round(player, dealer)

		elif player.winner == player.name +' busted!' or dealer.winner == 'Dealer busted!':
			if player.winner == player.name +' busted!':
				dealer.winner = 'Dealer wins!'
				self.end_round(player, dealer)
			else:
				player.winner = player.name + ' wins!'
				self.end_round(player, dealer)

		elif player.winner == player.name + ' wins!' or dealer.winner == 'Dealer wins!':
			if player.winner == player.name +' wins!':
				self.end_round(player, dealer)
			else:
				self.end_round(player, dealer)



	def set_count(self, whos_turn, points):
		if points == 0:
			print '!!!! 0 points !!!!'
		if points == 11:
			whos_turn.trackAces.append(points)
		if len(whos_turn.trackAces) > 0:
			for aces in range(len(whos_turn.trackAces)):
				if (whos_turn.count + points) > 21:
					whos_turn.count -= 10
					whos_turn.trackAces.pop()
		whos_turn.count += points


# Deal cards, first round deal 2 cards each then deal according to player's
# choice and dealer's rules.
	def game_deal_cards(self,deck,player,dealer, number_of_cards_to_deal, first_round):
		for n in range(number_of_cards_to_deal):
			#deal player cards
			if player.player_to_bet() and not player.stay:
				card_draw1 = deck.dealhand()
				self.player_hand.append(card_draw1)
				self.set_count(player,card_draw1[2])

			if dealer.dealer_to_bet():
				if first_round or player.stay:
					card_draw2 = deck.dealhand()
					self.dealer_hand.append(card_draw2)
					self.set_count(dealer, card_draw2[2])

		self.check_points(player,dealer)



