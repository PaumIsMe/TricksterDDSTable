from ddstable import ddstable

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]
RANKS = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
VALUE_BY_WORD = {
    "Two": "2",
    "Three": "3",
    "Four": "4",
    "Five": "5",
    "Six": "6",
    "Seven": "7",
    "Eight": "8",
    "Nine": "9",
    "Ten": "T",
    "Jack": "J",
    "Queen": "Q",
    "King": "K",
    "Ace": "A"
}


def hand_to_pbn(hand):
    cards_by_suit = {suit: '' for suit in SUITS}
    for card in hand:
        value_word, suit = card.split() # Ex: 'two', 'Spades
        value = VALUE_BY_WORD[value_word]
        cards_by_suit[suit] += value
    
    constructed_hand_pbn = f"{cards_by_suit['Spades']}.{cards_by_suit['Hearts']}.{cards_by_suit['Diamonds']}.{cards_by_suit['Clubs']}"
    return constructed_hand_pbn


def card_list_to_pbn(all_hands):

    assert(len(all_hands) == 52)

    north_hand = hand_to_pbn(all_hands[13*2:13*3])
    east_hand = hand_to_pbn(all_hands[13*3:13*4])
    south_hand = hand_to_pbn(all_hands[13*0:13*1])
    west_hand = hand_to_pbn(all_hands[13*1:13*2])

    #print(north_hand)
    #print(east_hand)
    #print(south_hand)
    #print(west_hand)

    return f"N:{north_hand} {east_hand} {south_hand} {west_hand}"

def print_table(PBN):
    all = ddstable.get_ddstable(PBN)
    print("{:>5} {:>5} {:>5} {:>5} {:>5} {:>5}".format("", "S", "H", "D", "C", "NT"))
    # may use  card_suit=["C", "D", "H", "S", "NT"]
    for each in all.keys():
        print("{:>5}".format(each),end='')
        for suit in ddstable.dcardSuit:
            trick=all[each][suit]
            if trick>7:
                print(" {:5}".format(trick - 6),end='')
            else:
                print(" {:>5}".format("-"),end='')
        print("")

def get_trickster_card_list(input_filename):
    # Load the text from 'in.txt' in the same directory
    with open(input_filename, "r", encoding="utf-8") as file:
        html = file.read()

    card_order = []

    for suit in SUITS:
        for rank in RANKS:
            card_identifying_substring = f"face {rank} {suit}"
            card_order.append( (html.find(card_identifying_substring), card_identifying_substring) )
        
    card_order.sort()
    card_list = [c[5:] for idx, c in card_order]
    return card_list

card_list = get_trickster_card_list("in.txt")
PBN = card_list_to_pbn(card_list)
print(PBN)
PBN = PBN.encode('utf-8')
#PBN_old = b"E:QJT5432.T.6.QJ82 .J97543.K7532.94 87.A62.QJT4.AT75 AK96.KQ8.A98.K63"
print_table(PBN)

print(dir(ddstable))