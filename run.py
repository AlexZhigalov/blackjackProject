from Ui import *
from Deck import *
from Player import *
from Dealer import *
from GameFlow import *

dealer = Dealer()
deck = Deck()
ui = Ui()
game = GameFlow()

#Ask player's name:
name = raw_input("Enter player's name: ")
#Ask player's bank:
total_bank = int(raw_input("Enter your bank amount: "))

player = Player(name, total_bank)

#Create new cards deck
deck.createdeck()

while True:
	game.round_reset(player,dealer)
	#Ask for player's bet
	player.set_bet(player)
	os.system('clear')
	ui.printGame(player,dealer,game.player_hand,game.dealer_hand, game, deck)
	game.game_deal_cards(deck,player,dealer, 2, True)
	os.system('sleep 2')
	os.system('clear')
	player.bet_accepted = ''
	#deal first round of two cards
	#dealer.hide_first_card = True

	# hide dealer's first card
	dealer.first_card_display(game)
	ui.printGame(player,dealer,game.player_hand,game.dealer_hand, game, deck)

	while game.round:
		next_move = raw_input('HIT(h) or STAY(s): ').lower()
		game.first_hand = False
		if next_move.startswith('h'):
			player.stay = False
			os.system('clear')
			game.game_deal_cards(deck,player,dealer, 1, False)
			dealer.first_card_display(game)
			ui.printGame(player,dealer,game.player_hand,game.dealer_hand, game, deck)
		if next_move.startswith('s'):
			player.stay = True
			while game.round:
				os.system('clear')
				dealer.hide_first_card = False
				dealer.first_card_display(game)
				ui.printGame(player,dealer,game.player_hand,game.dealer_hand, game, deck)
				os.system('sleep 0.5')
				os.system('clear')
				game.game_deal_cards(deck,player,dealer, 1, False)
				ui.printGame(player,dealer,game.player_hand,game.dealer_hand, game, deck)

