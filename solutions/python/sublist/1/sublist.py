"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 'Sublist'
SUPERLIST = 'Superlist'
EQUAL = 'Equal'
UNEQUAL = 'Unequal'

def equal(l1, l2):
    len_check = len(l1) == len(l2)
    return len_check and all([x == y for x, y in zip(l1, l2)])

def subset(l1, l2):
    n1 = len(l1)
    n2 = len(l2)
    i = 0
    while i <= (n2 - n1):
        if equal(l1, l2[i:n1+i]):
            return True
        i += 1
    return False

def superset(l1, l2):
    n1 = len(l1)
    n2 = len(l2)
    i = 0
    while i <= (n1 - n2):
        if equal(l1[i:n2+i], l2):
            return True
        i += 1
    return False

def sublist(list_one, list_two):
    if equal(list_one, list_two):
        return EQUAL
    elif subset(list_one, list_two):
        return SUBLIST
    elif superset(list_one, list_two):
        return SUPERLIST
    else:
        return UNEQUAL
        
    
            
   
            
        


   
    