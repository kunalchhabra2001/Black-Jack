import random

suits=('Hearts','Diamonds','Spades','Clubs')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','King','Queen','Ace')
values={'Two':2, 'Three': 3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10 , 'King':10, 'Ace':11}

playing=True
total=100

class Card():

	def __init__(self,suits,ranks):
		self.suits=suits
		self.ranks=ranks
	def __str__(self):
		return (self.ranks + ' of ' + self.suits)

class Deck():
    
    
    def __init__(self):
        self.deck=[] #We started with an Empty String
        
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        Card_command=''
        
        for card in self.deck():
            Card_command= Card_command + '\n' + 'card.__str__'
            return 'The deck has: ' + Card_command
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        single_card=self.deck.pop()
        return single_card

class Hand():

 	def __init__(self):
 		self.cards=[] #We start with an empty list
 		self.value=0 #Total sum of values of the cards in Hand
 		self.aces=0 #Keeps a count of total Aces in Hand

 	def add_Card(self,card):
 		#card itself is from Deck.deal() --> This card is of the form Card(suit,rank)
 		self.cards.append(card)
 		self.value += values[card.ranks]

 		#Keep a track of aces
 		if card.ranks=='Ace':
 			self.aces+=1

 	def adjust_for_ace(self):
 		while self.aces and self.value>21:
 			self.value -=10
 			self.aces -=1

class Chips():

 	def __init__(self,total=100):
 		self.total=total #Any Default Value
 		self.bet=0 #Can be adjusted as per the user

 	def win_bet(self):
 		self.total +=self.bet
 	def lose_bet(self):
 		self.total -=self.bet



def take_bet(chips):
 	while True:
 		try:
 			chips.bet = int(input('Please enter the amount you want to bet: ' ))
 		except ValueError:
 			print('Whoops!Please enter an integer not greater than your balance amount')
 		else:
 			if chips.bet > chips.total:
 				print('Sorry! Your current balance is {}'.format(chips.total))
 			else:
 				break


def hit(deck,hand):
 	added_card=deck.deal()
 	hand.add_Card(added_card)
 	hand.adjust_for_ace()

def hit_or_stand(deck,hand):
 	global playing
 	while True:

 		move = input('Hit Yes if you want to Hit,Else press No: ')
 		if move.lower()=='yes':
 			print('\n'*100)
 			hit(deck,hand)

 		elif move.lower()=='no':
 			print('\n'*100)
 			playing=False
 		else:
 			print('Sorry,I didnt get ur intention')

 		break

def show_some(player,dealer):
 	print('DEALERS Hand: ')
 	print('One card Hidden! ')
 	print(dealer.cards[1])
 	print('\n')
 	print('PLAYERS Hand: ')
 	for card in player.cards:
 		print(card)

def show_all(player,dealer):
 	print('Dealers Hand: ')
 	for card in dealer.cards:
 		print(card)
 	print('\n')
 	print('Players Hand: ')
 	for card in player.cards:
 		print(card)




def player_busts(player,dealer,chips):
 	print('BUST PLAYER')
 	chips.lose_bet()

def player_wins(player,dealer,chips):
 	print('WINS THE PLAYER')
 	chips.win_bet()

def dealer_busts(player,dealer,chips):
 	print('BUST DEALER')
 	chips.win_bet()
def dealer_wins(player,dealer,chips):
 	print('WINS DEALER')
 	chips.lose_bet()
def push(player,dealer):
 	print('Player and dealer push')




while True:

	# Print an opening statement
	print('Hey Gamblers,Welcome to BlackJack!')
	deck = Deck()

	#Create & shuffle the deck, deal two cards to each player
	deck.shuffle()
	player_hand = Hand()
	player_hand.add_Card(deck.deal())
	player_hand.add_Card(deck.deal())

	dealer_hand = Hand()
	dealer_hand.add_Card(deck.deal())
	dealer_hand.add_Card(deck.deal())

	# Set up the Player's Chips
	player_chips = Chips(total)

	#Prompt the Player for their bet
	take_bet(player_chips)

	#Show the cards, But keep one dealer's card hidden
	show_some(player_hand,dealer_hand)


	while playing: 

		#Prompt for player to hit or stand
		hit_or_stand(deck,player_hand)

		#Show the updated cards while keeping one Dealer's card hidden
		show_some(player_hand,dealer_hand)

		#If player's hand exceeds 21, Bust the player and break the loop
		player_hand.adjust_for_ace()

		if player_hand.value > 21:
			player_busts(player_hand,dealer_hand,player_chips)
			playing=False
	#if Player's hand is less than 21, Start updating the dealer's hand unless it exceeds Soft 17
	if player_hand.value <= 21:
		while dealer_hand.value<17:
			hit(deck,dealer_hand)

		#Show All of the cards in both hands to declare the final result
		show_all(player_hand,dealer_hand)

		#All the Winning or Losing Conditions: End of Game Scenario
		if player_hand.value > dealer_hand.value:
			player_wins(player_hand,dealer_hand,player_chips)

		elif dealer_hand.value > 21:
			dealer_busts(player_hand,dealer_hand,player_chips)

		elif player_hand.value < dealer_hand.value:
			dealer_wins(player_hand,dealer_hand,player_chips)
		else:
			push(player_hand,dealer_hand)

	#Print the User's Updated Balance And Ask if they wanna Play again
	print('\nHey user,You currently have {} chips'.format(player_chips.total))


	new_game = input('Would you like to play again? Reply with a y or n: ')
	if new_game[0].lower() == 'y':
		playing=True
		total = player_chips.total
		continue
	else:
		print('Thanks for playing!')
		break





