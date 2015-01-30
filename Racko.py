from random import randint

def shuffle(card):
    '''shuffle the card'''
    shuffled=range(1,61)
    for i in range(0,60):
        index=randint(0,59)      #pick a random index
        shuffled[i]=card[index]
    # =========ffor testing purpose=========
    # print shuffled
    # print len(shuffled)
    return shuffled

def does_user_begin():
    '''if coin shows head, namely if we get one, then user goes first'''
    if randint(0,1)==0:    # toss a coin, if 0 means computer goes first
        return True
    else:
        return False

def print_top_to_bottom(rack):
    '''print from top to bottom'''
    for i in range(0, len(rack)):
        print rack[i]


def main():
    global deck
    global discard

    deck=range(1,61)
    computer=[]
    user=[]
    deck=shuffle(deck)
    #deal a card to the computer and a card to the user
    #repeat unitl both have 10 cards
    for i in range(0,20,2):
        computer.append(deck[i])
        user.append(deck[i+1])
    #=========for testing purpose=========
    #print computer
    #print user

    #choose who goes first
    if does_user_begin()==True:
        '''Print from top to bottom'''
        print_top_to_bottom(user)
        
        

    

    
        
    
    
    

if __name__=='__main__':
    main()


    

    
