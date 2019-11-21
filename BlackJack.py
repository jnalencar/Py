# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
boole = False
pos = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cardlist = []
        self.num = 0
        
    def __str__(self):
        string = ''
        for card in self.cardlist:
            string = string + card.suit + card.rank + ' '
        return 'Hand contains '+string	# return a string representation of a hand

    def add_card(self, card):
        self.cardlist.append(card)
        self.num = self.num + VALUES[card.rank]# add a card object to a hand

    def get_value(self):
        total = 0
        for card in self.cardlist:
            total = total + VALUES[card.rank]
        for card in self.cardlist:	
            if card.rank == 'A' and total + 10 <= 21:
                return total + 10
        return total
    def draw(self, canvas, pos, boole):
        if not boole:
            card_loc = (CARD_CENTER[0], 
                        CARD_CENTER[1])
            canvas.draw_image(card_back, card_loc, CARD_SIZE, (pos[0], pos[1]), CARD_SIZE)
        else:
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.cardlist[0].rank), 
                        CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.cardlist[0].suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, (pos[0], pos[1]), CARD_SIZE)
        for i in range(len(self.cardlist) - 1):
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.cardlist[i+1].rank), 
                        CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.cardlist[i+1].suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, (pos[0] + ((i+1)*(CARD_SIZE[0])), pos[1]), CARD_SIZE) # draw a hand on the canvas, use the draw method for cards
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.cardlist = []
        for rank in RANKS:
            for suit in SUITS:
                self.cardlist.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.cardlist)

    def deal_card(self):
        return self.cardlist.pop()
    
    def __str__(self):
        string = ''
        for card in self.cardlist:
            string = string + card.suit + card.rank + ' '
        return 'Deck constains '+string




#define event handlers for buttons
deck = Deck()
player_hand = Hand()
dealer_hand = Hand()
def deal():
    global outcome, in_play, player_hand, dealer_hand, boole

    # your code goes here
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    for i in range(2):
        player_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())
    print 'Player '+str(player_hand)
    print 'Player Score: ',player_hand.get_value()
    print 'Dealer '+str(dealer_hand)
    print 'Dealer Score: ',dealer_hand.get_value()
    in_play = True
    boole = False
    outcome = ''

def hit():
    global in_play, player_hand, dealer_hand, boole, score, outcome, pos
    # if the hand is in play, hit the player
    if in_play:	
        player_hand.add_card(deck.deal_card())
    # if busted, assign a message to outcome, update in_play and score
        print 'Player Score: ',player_hand.get_value()
        print 'Player '+str(player_hand)
        print 'Dealer Score: ',dealer_hand.get_value()
        print 'Dealer '+str(dealer_hand)
    if player_hand.get_value() > 21 and in_play:
        pos = 0
        outcome = 'Player busted, Dealer won!'
        in_play = False
        boole = True
        score -= 1
def stand():
    global in_play, player_hand, dealer_hand, boole, outcome, score, pos
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer_hand.get_value() <= 17:
            dealer_hand.add_card(deck.deal_card())
    # assign a message to outcome, update in_play and score
    if player_hand.get_value() <= 21 and dealer_hand.get_value() > 21 and in_play:
        pos = 0
        outcome = 'Dealer busted, Player won!'
        in_play = False
        boole = True
        score += 1
    elif player_hand.get_value() > dealer_hand.get_value() and in_play:
        pos = 80
        outcome = 'Player wins!'
        in_play = False
        boole = True
        score += 1
    elif in_play:
        pos = 80
        outcome = 'Dealer wins!'
        score -= 1
        in_play = False
        boole = True
    
# draw handler    
def draw(canvas):
    global outcome, in_play, pos
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text('BlackJack', [237, 50], 35, 'Red', 'sans-serif')
    player_hand.draw(canvas, [100, 450], True)
    dealer_hand.draw(canvas, [100, 150], boole)
    canvas.draw_text('You have '+str(player_hand.get_value())+' points.', [64, 518], 20, 'Red')
    canvas.draw_text(outcome, [125 + pos,300], 37, 'White')
    if in_play:
        canvas.draw_text('Hit or Stand?', [200, 300], 37, 'Black')
    else:
        canvas.draw_text('New Deal?', [220, 350], 37, 'Black')
    canvas.draw_text('Your score: '+str(score), [450, 100], 25, 'White')
    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric
