#authors - Yike Chen and Xiaozhuo Cheng
import random

def shuffle():
    '''shuffle the card'''
    global deck
    global discard
    if len(deck)==60:
        random.shuffle(deck)
    if len(deck)==0:
        random.shuffle(discard)
        deck=discard
        discard=[]
        discard.append(deal_card())

def deal_initial_hands():
    '''Start the game by dealing two hands of 10 cards each'''
    i=0
    computer=[]
    user=[]
    while i<10:
        computer.append(deck.pop(-1))
        user.append(deck.pop(-1))
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
    return deck.pop(-1)

def check_racko(racko):
    '''Determine if racko has been reached'''
    n=0
    for i in range(1,10):
        if racko[i-1]>racko[i]:
            n=n+1
    if n==9:
        print 'Racko!'
        return True
    else:
        return False

def computer_play(hand):
    x=0
    j=0
    print '''Now is computer's turn!'''
    print '''> > > > > > >  P L E A S E    W A I T  < < < < < < < '''
    # divide 1~60 into 10 sections, compare each card with each section, if the discard card is more suitable, then change into discard card
    for i in range(9,-1,-1):
        if (x==0)and( (  (j<discard[-1]<=j+6) and (hand[i] not in range(j+1,j+7)) ) or ( (j<discard[-1]<=j+6) and (hand[i]>discard[-1] ))    ):
            x=hand.pop(i)
            hand.insert(i,discard[-1])
            discard.pop(-1)
            discard.append(x)
        j+=6
    j=0
    # if this does not work, then try card from deck pile
    if x==0:
        for k in range(9,-1,-1):
            if (x==0) and ((  (j<deck[-1]<=j+6) and (hand[k] not in range(j+1,j+7) ) )or ( (j<deck[-1]<=j+6) and (hand[k]>deck[-1] ))    ):
                x=hand.pop(k)
                hand.insert(k,deck[-1])
                deck.pop(-1)
                discard.append(x)           
            j+=6
    if x==0:
        x=deck.pop(-1)
        discard.append(x)
    return hand

def find_and_replace(newCard, cardToBeReplaced, hand):
    '''FInd the card to be replaced in the hand and replace it with new card'''

    while (not (int(cardToBeReplaced) in hand)):
        cardToBeReplaced=raw_input('You received this message because the card is not even in your hand.\n Which card do you wish to kick out this time?  ')
    
    #modify the user's hand and the discard pile
    index=hand.index(int(cardToBeReplaced))
    hand.pop(index)
    hand.insert(index,newCard)
    discard.append(int(cardToBeReplaced))
    #print the user's hand
    print_top_to_bottom(hand)

def add_card_to_discard(card):
    discard.append(card)

def main():
    global deck
    global discard
    deck=range(1,61)
    discard=[]
    #Set a flag to indicate whether it is the first round or not
    initial_round=True 
    #shuffle the deck of card
    shuffle()

    #deal a card to the computer and a card to the user
    #repeat unitl both have 10 cards
    (computer_hand,user_hand)=deal_initial_hands()

    #choose who goes first
    userStarts=does_user_begin()
    if userStarts==True:
        print '''User starts first!'''
        who_starts_first='User'
    else:
        print '''Computer starts first!'''
        who_starts_first='Computer'
    print '''Deal initial hands complete: '''
    print_top_to_bottom(user_hand)
    add_card_to_discard(deal_card())
          
    #while neither the computer nor the user has racko
    while (not (check_racko(computer_hand))) and (not (check_racko(user_hand))):
        if (who_starts_first=='Computer') and initial_round:
            computer_hand=computer_play(computer_hand)
        #ask the user if they want this card
        #print the user's hand
        print
        print 'Now it is your turn! '
        print_top_to_bottom(user_hand)
        print 'discard card:', discard[-1]
        choice=raw_input('Do you want this card? Input \'Y\' if you do, \'N\' if you do not.')
        if choice in 'Yy':
            #ask the user for the number of the card they want to kick out
            unwanted=raw_input('From top to bottom, which card do you wish to kick out? ')
            #find the card and replace it, update the discard pile, then print the user's hand
            replace=discard.pop(-1)
            find_and_replace(replace,unwanted,user_hand)
            
        elif choice in 'Nn':
            card=deck.pop(-1)
            print 'The card you get from the deck is ', card
            #ask the user if he wants to use it
            choice2=raw_input('Do you want to keep it? ')
            if choice2 in 'Yy':
                #modify users hand, the discard pile and then print user's hand
                unwanted2=raw_input('From top to bottom, which card do you wish to kick out? ')
                find_and_replace(card,unwanted2,user_hand)
            else:
                add_card_to_discard(card)
                print_top_to_bottom(user_hand)
        #check if user reaches racko
        if (check_racko(user_hand)):
            print '''========= Congrats, you win! ============'''
            break
        #when the user has no card from the deck, there is no need for computer to proceed
        shuffle()
        computer_hand=computer_play(computer_hand)
        #check if computer reaches racko
        if (check_racko(computer_hand)):
            print '''========= Sucker, you lose! ==========='''
            break
        
        #change the flag to indicate it is no longer first round          
        initial_round=False               
        #check and make sure there are still some cards in the deck
        shuffle()


        
    #Restart the game
    print '\n'*33
    main()

if __name__=='__main__':
    main()


    

    
