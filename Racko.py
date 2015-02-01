import random

def shuffle():
    '''shuffle the card'''
    random.shuffle(deck)        
    # =========for testing purpose=========
    print deck
    #=================================

def deal_initial_hands():
    '''Start the game by dealing two hands of 10 cards each'''
    i=0
    computer=[]
    user=[]
    while i<10:
        computer.append(deck.pop(0))
        user.append(deck.pop(0))
        i+=1
    return (computer, user)
    

def does_user_begin():
    '''if coin shows head, namely if we get one, then user goes first'''
    if random.randint(0,1)==0:    # toss a coin, if 0 means computer goes first
        return True
    else:
        return False

def print_top_to_bottom(rack):
    '''print from top to bottom'''
    print '''Here are your cards:'''
    for i in range(0, len(rack)):
        print rack[i]

def deal_card():
    '''Get the top card from the deck'''
    return deck.pop(0)

def check_racko(racko):
    '''Determine if racko has been reached'''
    n=0

    for i in range(1,10):
        if racko[i-1]<racko[i]:
            n=n+1
    if n==9:
        # =========for testing purpose=========
        print 'Racko!'
        #=================================
        return True
    else:
        return False

def computer_play(hand):
    if (discard[-1]>50) and (discard[-1]>hand[-1]):
        hand.pop(-1)
        hand.append(discard[-1])
    elif (discard[-1]>40) and (discard[-1]>hand[-2]):
        hand.pop(-2)
        hand.insert(-2,discard[-1])
    elif (discard[-1]>30) and (discard[-1]>hand[-3]):
        hand.pop(-3)
        hand.insert(-3,discard[-1])
    elif (discard[-1]>20) and (discard[-1]>hand[-4]):
        hand.pop(-4)
        hand.insert(-4,discard[-1])
    print hand
    
def find_and_replace(new_Card, cardToBeReplaced, hand):
    '''FInd the card to be replaced in the hand and replace it with new card'''
    print '''Did you mean this card? ''', cardToBeReplaced
    confirm=raw_input('Please input \'Y\' if it is right, \'N\' if it is not. ')


    while (confirm in 'Nn' ) or (not (int(cardToBeReplaced) in hand)):
        cardToBeReplaced=raw_input('You received this message because either you entered \'N\' or the card is not even in your hand.\n Which card do you wish to kick out this time?  ')
        print '''Did you mean this card? ''', cardToBeReplaced
        confirm=raw_input('Please input \'Y\' if it is right, \'N\' if it is not. ')
    
    #modify the user's hand and the discard pile
    index=hand.index(int(cardToBeReplaced))
    hand.pop(index)
    discard.pop(-1)    
    hand.insert(index,new_Card)
    discard.append(int(cardToBeReplaced))
    #print the user's hand
    print_top_to_bottom(hand)


def main():
    global deck
    global discard

    deck=range(1,61)
    discard=[]

    initial_round=True
    
    #shuffle the deck of card
    shuffle()
    
    #deal a card to the computer and a card to the user
    #repeat unitl both have 10 cards
    (computer_hand,user_hand)=deal_initial_hands()

    #=========for testing purpose=========
    print computer_hand
    print user_hand
    #=================================

    #choose who goes first
    userStarts=does_user_begin()
    if userStarts==True:
        print '''User starts first!\n'''
        who_starts_first='User'
    else:
        print '''Computer starts first!\n'''
        who_starts_first='Computer'

    print_top_to_bottom(user_hand)
        
    #=========for testing purpose=========
    #reveal one card to begin the discard pile
    discard.append(deal_card())
    #print '''discard card:''', discard[-1]
    #=================================

        
    #while neither the computer nor the user has racko
    computer_racko=check_racko(computer_hand)
    user_racko=check_racko(user_hand)

    while (not computer_racko) and (not user_racko):
        if (who_starts_first=='Computer') and initial_round:
            computer_hand=computer_play(computer_hand)

        #ask the user if they want this card
        #print the user's hand
        print
        print_top_to_bottom(user_hand)
        print 'discard card:', discard[-1]
        choice=raw_input('Do you want this card? Input \'Y\' if you do, \'N\' if you do not.')
        if choice in 'Yy':
            #ask the user for the number of the card they want to kick out
            unwanted=raw_input('From top to bottom, which card do you wish to kick out? ')
            #find the card and replace it, update the discard pile, then print the user's hand
            find_and_replace(discard[-1],unwanted,user_hand)
        elif choice in 'Nn':
            card=deck.pop(0)
            print 'The card you get from the deck is ', card
            #ask the user if he wants to use it
            choice2=raw_input('Do you want to keep it? ')
            if choice2 in 'Yy':
                #modify users hand, the discard pile and then print user's hand
                unwanted2=raw_input('From top to bottom, which card do you wish to kick out? ')
                find_and_replace(card,unwanted2,user_hand)
            else:
                discard.append(card)
                print_top_to_bottom(user_hand)
        
        computer_hand=computer_play(computer_hand)

        #change the flag           
        initial_round=False               
        #check and make sure there are still some cards in the deck
        if len(deck)==0:
            shuffle()
        #restart the game
            
 

if __name__=='__main__':
    main()


    

    
