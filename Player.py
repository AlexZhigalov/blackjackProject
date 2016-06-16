import os

class Player(object):


	def __init__(self, name, bank):
		self.name = name
		self.bank = bank
		self.bet = 0
		self.count = 0
		self.trackAces = []
		self.winner = ''
		self.stay = False
		self.bet_accepted = ''

	def player_to_bet(self):
		if self.count  < 21:
			return True
		else:
			return False


	def bank_substract(self):
		self.bank -= self.bet

	def bank_add(self):
		self.bank += self.bet*2

	def set_bet(self, player):
		while True:
			try:
				self.bet = int(raw_input('Set your bet: '))
			except:
				print 'Wrong Input, intirgers only. Try again!'
				continue
			else:
				self.bet_accepted = player.name + "'s bet of "+str(self.bet)+"$ excepted. DEALING CARDS!"
				self.bank_substract()
				break