#
# An OO Design to Implement a Deck of 52 cards
#   by Charles Gust
#
#  Card: Holds "rank" and "suit" paired to identify a card.
#  Deck: Holds a list of cards
#
#
# An alternative implementation may be to simply use integers to represent
#  the cards in an absolute order, ie, 0 to 51 would correspond to particular
#  cards with suit and rank in a French Deck of 52 cards. This would be a very
#  fast and space efficient representation, but has certain problems:
#   - Generally not as emblematic of OO Design
#   - Deck would constrained to French Deck (52 cards)
#
#   If a later implementation requires decoding integers for cards remember
#     it's more efficient to use (mod 4) and (div 4) than (mod 13) and (div 13)
#     to translate integer numbers into cards from a French Deck.
#
from random import random


class Card():
    rank_display = ['A', '2', '3', '4', '5', '6',
                    '7', '8', '9', '10', 'J', 'Q', 'K']
    suit_display = ['Spades', 'Diamonds', 'Clubs', 'Hearts']

    # CMGTODO: may be overkill to have num_suits() as a method
    @staticmethod
    def num_suits():
        """ count suits defined for deck """
        return len(Card.suit_display)

    # CMGTODO: may be overkill to have num_ranks() as a method, particularly
    #  since not all decks use all ranks
    @staticmethod
    def num_ranks():
        """ count ranks defined for deck, ie for each suit """
        return len(Card.rank_display)

    @staticmethod
    def check(possibly_card):
        """ helps functions that require only a card by raising exception if not """
        if not isinstance(possibly_card, Card):
            raise ValueError("%s is not a Card" % (possibly_card,))
        return possibly_card

    def __init__(self, rank, suit):
        """ identify a card by rank and suit """

        # CMGTODO: In Euchre and Pinochle, anything 2-8 isn't allowed
        #  so perhaps if is just overhead to check at here __init__
        if (rank < 0) or (rank > Card.num_ranks()):
            raise IndexError("rank out of bounds")
        self.rank = rank

        if (rank < 0) or (suit > Card.num_suits()):
            raise IndexError("suit out of bounds")
        self.suit = suit


    def __getitem__(self, key):
        """ allow [0] to access rank, [1] to access suit """
                # CMGTODO: any key except 0 gets suit; should raise IndexError?
        return self.rank if key == 0 else self.suit

    def __setitem__(self, key, item):
        """ allow [0] to set rank, [1] to set suit """

        # CMGTODO: does not check for bounds or type. Should it?
        # CMGTODO: any key except 0 sets suit; should raise IndexError?
        if key == 0:
            self.rank = item
        else:
            self.suit = item

    def __repr__(self):
        """ display card as a tuple of rank and suit """
        # Regarding representing the card as a tuple or an array (of elements
        # rank and suit), a tuple was chosen to convey the notion that
        # the elements themselves are not to be changed.
        return "(%s, %s)" %\
            (Card.rank_display[self.rank], Card.suit_display[self.suit])

    def __str__(self):
        """ display human English readable card name """
        return "%s of %s" % \
            (Card.rank_display[self.rank], Card.suit_display[self.suit])

    # normally, no value of a card could be defined in the class Card
    # because the value of a card is game dependent, and may even possibly
    # have multiple values simultaneously depending on the rules of the
    # game. This function provides the most common values.
    # There are also games were the cards values depend on suit or depend
    # on how they are played.
    # This function also reminds users of this class that the rank is zero-
    # indexed, which means one must be added for most card game values
    def value(self, ace_high=False, face_cards_same=False):
        """ determine value of card for some games (based on rank) """
        if ace_high or face_cards_same:
            # 'J' is rank == 10, 'K' is rank == 12
            if face_cards_same and (self.rank >= 10) and (self.rank <= 12):
                return 10

            # 'A' is rank == 0
            if ace_high and (self.rank == 0):
                return 11

        # otherwise, card rank is zero indexed and add one for value
        return self.rank + 1


#
# A Deck is an collection (ie, list) of cards
#
# Multiple Deck objects may be used in a game to represent players held
# cards, discard piles, played cards, however because __getitem__ defines
# the '[]' operators this way, an array of Decks is not supported.
#
class Deck():
    """ define a collection (ie, list) of cards """
    def __init__(self):
        self.deck = []

    def init_FrenchDeck(self):
        """ init French deck with 52 cards """
        self.deck.extend([Card(rank, suit)
                         for rank in xrange(Card.num_ranks())
                         for suit in xrange(Card.num_suits())])

    def init_EuchreDeck(self):
        """ init Euchre deck with 24 cards """
        self.deck.extend([Card(rank, suit)
                         for rank in [0, 8, 9, 10, 11, 12]
                         for suit in xrange(Card.num_suits())])

    def init_PinochleDeck(self):
        """ init Pinochle deck with 48 cards """
        for count in xrange(2):
            self.init_EuchreDeck()

    def __getitem__(self, key):
        """ allow direct indexing of cards within the deck """
        return self.deck[key]

    def __setitem__(self, key, item):
        """ allow changes to a deck, for instance, a discard pile """
        self.deck[key] = Card.check(item)

    def __repr__(self):
        """ display deck as array of tuples from bottom to top of deck """
        return "%s" % [self.deck[card] for card in xrange(len(self.deck))]

    def __str__(self):
        """ display deck as human English readable from bottom to top of deck """
        return "%s" % [self.deck[card].__str__() for card in xrange(len(self.deck))]

    def remove_card(self, removeable_card):
        """ remove a card from a deck, useful when moving it to another """
        self.deck.remove(Card.check(removeable_card))

    def append_card(self, appendable_card):
        """ pushes the next card onto a deck at the end of the list LI of LIFO """
        self.deck.append(Card.check(appendable_card))

    def index_card(self, indexable_card):
        """ find a card in a deck """
        self.deck.index(Card.check(indexable_card))

    def place_on_bottom(self, insertable_card):
        """ move a card to the bottom of a deck, which is the head of the list FI of LIFO"""
        # This could be an expensive operation, but there is at least
        # one card game, War, where the discards get placed on the bottom
        # of the players hand/deck to be played again.
        self.deck.insert(0, Card.check(insertable_card))

    def deal_next_card(self):
        """ pops the next card off a deck, which is at the end of the list FO of LIFO"""
        return self.deck.pop()

    def shuffle(self):
        """ shuffles a deck by performing random number of card exchanges """
        decklen = len(self.deck)

        # it makes sense to have the number of cards exchanged grow as
        #  the number of cards in the deck grows.
        for shuffle_count in xrange((decklen*10) + int(random() * decklen * 5)):
            card1 = int(random() * decklen)
            card2 = int(random() * decklen)

            swap_val = self.deck[card1]
            self.deck[card1] = self.deck[card2]
            self.deck[card2] = swap_val
