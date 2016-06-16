from Deck import *
from Player import *
import os

class Ui(object):

	def __init__(self):
		self.temp = ['   ' + '_ _ _ _  ',
		'  ' + '|'+ ' '*8 + '|',
		'  ' + '|'+ ' '*8 + '|','','',
		'  ' + '|'+ ' '*8 + '|',
		'  ' + '| _ _ _ _|']

	def printcards(self, cards):
		'''
		Takes cards from the deck and prints them out in one line
		:param cards: list of cards(tuples) from the deck of cards
		:return: prints passed cards in one line
		'''

		final_print = ['']*7
		for h in cards:
			for l in range(7):
				if l == 3:
					final_print[l] += '  ' + '|'+ cards[cards.index(h)][0].center(8) +'|'
				elif l == 4:
					final_print[l] += '  ' + '|'+ cards[cards.index(h)][1].center(8) +'|'
				final_print[l] += self.temp[l]
		if len(final_print) != 0:
			for l in final_print:
				print l


	def printGame(self,player,dealer, pl, dl, game, deck):
		print '='*90
		print player.name + "'s cards: " + ' '*20 + player.bet_accepted
		print ' '*75 + player.winner
		self.printcards(pl)
		print ''
		print ''
		print player.name + "'s points count: ",str(player.count) + \
				' '*15 + "Current bet: ",str(player.bet) + ' '*15 + player.name + "'s bank:", player.bank
		print ''
		print '-~'*45
		print ''
		print "Dealers's cards:"
		print ' '*75 + dealer.winner
		self.printcards(dl)
		print ''
		print ''
		print "Dealers's points count: " + str(dealer.points_to_display(game, player)) + ' '*20 + deck.new_deck
		print ''
		print '='*90