def sameAB(abstring):
    if len(abstring) == 0:
        return True
    if len(abstring)==1:
        return False
    if len(abstring)>1:
        if abstring[0]=='a' and abstring[-1]=='b':
            return True and  sameAB(abstring[1:len(abstring)-1])
        else:
            return False and sameAB(abstring[1:len(abstring)-1])

        
def binary_search(lst,val):
    middle_index = len(lst)/2
    if len(lst)==0:
        return False
    elif len(lst) == 1:
        if val == lst[0]:
            return True
        else:
            return False
    elif len(lst)>1:
        if val == lst[middle_index]:
            return True
        if val < lst[middle_index]:
            return binary_search(lst[0 : middle_index ],val)
        elif val > lst[middle_index]:
            return binary_search(lst[middle_index + 1 : ],val)


def flatten(lst_of_lst):
    if len(lst_of_lst) == 0  or len(lst_of_lst) == 1  :
        return lst_of_lst[0]
    elif len(lst_of_lst) > 1:
        return lst_of_lst[0]+flatten(lst_of_lst[1:])

        
def initials(lst):
    print [x.split()[0][0]+'.'+x.split()[1][0]+'.' for x in lst]


def meamers(filename):
    print len(['MEAMer' for line in open(filename) if line.rstrip().lstrip().split(',')[1]=='MEAM'])


def most_frequent_alphabet(frequency_dictionary):
    print [alphabet for alphabet in frequency_dictionary.keys() if frequency_dictionary[alphabet] == max(frequency_dictionary.values())]


##meamers('student.csv')
##most_frequent_alphabet({'a': 3,'b': 4,'c': 5,'d': 2,'e':13,'f': 2})






    
