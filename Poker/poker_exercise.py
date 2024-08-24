import random

class Card:
    def __init__(self, rank, suit):
        self.__rank = rank
        self.__suit = suit

    def get_rank(self):
        #return the rank of the card
        return self.__rank

    def get_suit(self):
        #return the suit of the card
        return self.__suit

    def get_value(self):
        #define card values. Number cards are their number value, face cards are 10, and Ace is 11.
        if self.__rank in ['J', 'Q', 'K']:
            return 10
        elif self.__rank == 'A':
            return 11
        else:
            return int(self.__rank)

    def __str__(self):
        return f"{self.__rank} of {self.__suit}"

class PokerHand:
    def __init__(self, cards=None):
        if cards is None:
            cards = []
        self.__cards = cards

    def add_card(self, card):
        #add a card to the hand
        self.__cards.append(card)

    def show_hand(self):
        #return a string representation of the hand
        return ', '.join(str(card) for card in self.__cards)

    def get_total_points(self):
        #calculate the total points of the hand
        return sum(card.get_value() for card in self.__cards)

class Deck:
    def __init__(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.__cards = [Card(rank, suit) for rank in ranks for suit in suits]
        random.shuffle(self.__cards)  # Shuffling the deck to randomize the order of cards

    def deal_card(self):
        #deal a card from the deck
        return self.__cards.pop()
class PokerGame:
    def __init__(self):
        self.deck = Deck()
        self.player1_hand = PokerHand()
        self.player2_hand = PokerHand()

    def deal_hands(self):
        for _ in range(3):
            self.player1_hand.add_card(self.deck.deal_card())
            self.player2_hand.add_card(self.deck.deal_card())

    def determine_winner(self):
        player1_points = self.player1_hand.get_total_points()
        player2_points = self.player2_hand.get_total_points()

        if player1_points > player2_points:
            return "Player 1 wins!"
        elif player2_points > player1_points:
            return "Player 2 wins!"
        else:
            return "It's a tie!"
    
    def play_game(self):
        self.deal_hands()
        print("Player 1's hand:", self.player1_hand.show_hand())
        print("Player 2's hand:", self.player2_hand.show_hand())
        print(self.determine_winner())

# Example usage:
game = PokerGame()
game.play_game()

