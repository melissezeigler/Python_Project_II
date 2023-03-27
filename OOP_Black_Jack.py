import random
class Blackjack:
    def __init__(self):
        pass
    def create_shuffled_deck(self):
        shuff_val = []
        shuff_suit = []
        self.shuff_deck = []
        i=0
        while i<52:
            randomcard = random.randint(1,52)
            if randomcard not in shuff_val:
                shuff_val.append(randomcard)
                i += 1
            else:
                i += 0
        m = 0
        while m<52:
            shuff_suit.append(shuff_val[m] % 4)
            m+=1
        k=0
        while k<52:
            shuff_val[k] = shuff_val[k] % 13
            k+=1
        j=0
        while j<52:
            self.shuff_deck.append([shuff_suit[j]+1, shuff_val[j]+1])
            j+=1
        p=0
        while p<len(self.shuff_deck):
            if self.shuff_deck[p][0] == 1:
                self.shuff_deck[p][0] = 'Spade'
            if self.shuff_deck[p][0] == 2:
                self.shuff_deck[p][0] = 'Diamond'
            if self.shuff_deck[p][0] == 3:
                self.shuff_deck[p][0] = 'Club'
            if self.shuff_deck[p][0] == 4:
                self.shuff_deck[p][0] = 'Heart'
            p+=1 
        return self.shuff_deck
    def play(self):
###########################starting sequence####################################
        deck = self.create_shuffled_deck()
        p_hand = [deck.pop()]
        p_hand.append(deck.pop())
        deal_hand = [deck.pop()]
        deal_hand.append(deck.pop())
        p_hand_val = (int(p_hand[0][1]) + int(p_hand[1][1]))
        deal_hand_val = (int(deal_hand[0][1]) + int(deal_hand[1][1]))
        not_bust = True
        if p_hand_val == 21:
            print(f'Blackjack acheived!! Your hand is {p_hand} for a value of {p_hand_val}.')
        elif p_hand_val > 21:
            print(f'Bust!! Your hand is {p_hand} for a value of {p_hand_val}.')
        else:
########################player hand sequence################################    
            while not_bust:
                stand_hit = input(f' Your hand is {p_hand} for a value of {p_hand_val}.\n The dealer is showing {deal_hand[1]}.\n Will you hit or stand? Type "Hit or Stand"')
            
                if stand_hit.lower() == "hit":
                    new_card = deck.pop()
                    p_hand.append(new_card)
                    p_hand_val = (p_hand_val + int(new_card[1]))
                    if p_hand_val >= 22:
                        print(f"BUST! You were dealt {new_card} bring your value to {p_hand_val}. Game over")
                        not_bust = False
                    else:
                        pass
#########################dealer hand sequence#############################                    
                if stand_hit.lower() == "stand" and deal_hand_val > 21:
                    print(f'You win! The dealer was dealt an insta-bust, with hand value {deal_hand_val}.')
                    not_bust = False    
                if stand_hit.lower() == "stand" and deal_hand_val >= 17 and deal_hand_val < 22:
                    if p_hand_val > deal_hand_val:
                        print(f'You win! The dealer hand value is {deal_hand_val}.')
                        not_bust = False
                    if p_hand_val <= deal_hand_val:
                        print(f'You lose. The dealer hand value is {deal_hand_val} (dealer wins in case of ties).')
                        not_bust = False
                if stand_hit.lower() == "stand" and deal_hand_val < 17 and not_bust == True:    
                    while deal_hand_val <17:
                        new_deal_card = deck.pop()
                        deal_hand.append(new_deal_card)
                        deal_hand_val = (deal_hand_val + int(new_deal_card[1]))
                        if deal_hand_val > 21:
                            print(f'You win! The dealer has gone bust, with a hand value of {deal_hand_val}.')
                            not_bust = False
                        if deal_hand_val <= 21 and deal_hand_val >= 17:
                            if p_hand_val > deal_hand_val:
                                print(f'You win! The dealer hand value is {deal_hand_val}')
                                not_bust = False
                            if p_hand_val <= deal_hand_val:
                                print(f'You lose. The dealer hand value is {deal_hand_val} (dealer wins in case of ties).')
                                not_bust = False
                        if deal_hand_val < 17:
                            pass
                    not_bust = False
bigmouth_billy_bass = Blackjack()
bigmouth_billy_bass.play()

