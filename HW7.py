def sameAB(abstring):
    
    while len(abstring) > 0:
        if abstring[0] == 'a':
            a_num += 1
        else:
            b_num += 1
        sameAB(abstring[1:])

    print a_num,b_num
    if a_num != b_num:
        return False
    else:
        return True

    

##def flatten(lst_of_lst):


##def binary_search(lst,val):

##def most_frequent_alphabet(frequency_dictionary):


##def meamers(filename):

##def initials(lst):

    
