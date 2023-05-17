import sys
import cards

def compair(card1,card2):
    '''Return 
           True if c1 is smaller in rank, 
           True if ranks are equal and c1 has a 'smaller' suit
           False otherwise'''
    if card1.get_rank() < card2.get_rank():
        return True
    elif card1.equal_rank(card2) and card1.get_suit() < card2.get_suit():
        return True
    return False
    
def index_of_min(newList):
    '''Return the index of the mininmum card in L'''
    mincard = newList[0]  # first card
    minindex = 0
    for index,card in enumerate(newList):  #enumerate(iterable, start=0) Iterable: any object that supports iteration Start: the index value
        if compair(card,mincard):  # found a smaller card, c
            mincard = card
            minindex = index
    return minindex
        
def slection(plyaercard):
    ''' Selection Sort: find smallest and swap with first in H,
        then find second smallest (smallest of rest) and swap with second in H,
        and so on...'''
    for index,card in enumerate(plyaercard): #enumerate(iterable, start=0) Iterable: any object that supports iteration Start: the index value
        # get smallest of rest; +i to account for indexing within slice
        min_index = index_of_min(plyaercard[index:]) + index 
        plyaercard[index], plyaercard[min_index] = plyaercard[min_index], card  # swap
    return plyaercard

def straight_flush_7(H):
    """
        Return a list of 5 cards forming a straight flush,
       if at least 5 of 7 cards form a straight flush in H, a list of 7 cards, 
       False otherwise.
    """
    new1 = []
    new2 = []
    new3 = []
    new4 = []
    for i in H:
        if i.get_suit() == 1:
            new1.append(i)
        elif  i.get_suit()==2:
            new2.append(i)
        elif i.get_suit() == 3:
            new3.append(i)
        elif i.get_suit() == 4:
            new4.append(i)
    if len(new1) >= 5:
        new = []
        for i in new1:
            i = i.get_rank()
            new.append(i)       
        x =  new[0]
        x1 = new[1]
        x2 = new[2]
        if (new[:5] == list(range(x,x+5))):
            m = [8]
            m1 = new1[:5] + m
            return m1
        elif (new[1:6] == list(range(x1,x1+5))):
            m = [8]
            m1 = new1[1:6] + m
            return m1
        elif (new[2:7] == list(range(x2,x2+5))):
            m = [8]
            m1 = new1[2:7] + m
            return m1            
        else:
            return four_7(H)
            
            
    elif len(new2) >= 5:
        new = []
        for i in new2:
            i = i.get_rank()
            new.append(i)       
        x = new[0]
        x1 = new[1]
        x2 = new[2]
        if (new[:5] == list(range(x,x+5))):
            m = [8]
            m1 = new2[:5] + m
            return m1
        elif (new[1:6] == list(range(x1,x1+5))):
            m = [8]
            m1 = new2[1:6] + m
            return m1
        elif (new[2:7] == list(range(x2,x2+5))):
            m = [8]
            m1 = new2[2:7] + m
            return m1
        else:
            return four_7(H)
     
    elif len(new3) >= 5:
        new = []
        for i in new3:
            i = i.get_rank()
            new.append(i)       

        x = new[0]
        x1 = new[1]
        x2 = new[2]
        if (new[:5] == list(range(x,x+5))):
            m = [8]
            m1 = new3[:5] + m
            return m1
        elif (new[1:6] == list(range(x1,x1+5))):
            m = [8]
            m1 = new3[1:6] + m
            return m1
        elif (new[2:7] == list(range(x2,x2+5))):
            m = [8]
            m1 = new3[2:7] + m
            return m1
        else:
            return four_7(H)
    elif len(new4) >= 5:
        new = []
        for i in new4:
            i = i.get_rank()
            new.append(i)       

        x = new[0]
        x1 = new[1]
        x2 = new[2]
        if (new[:5] == list(range(x,x+5))):
            m = [8]
            m1 = new4[:5] + m
            return m1
        elif (new[1:6] == list(range(x1,x1+5))):
            m = [8]
            m1 = new4[1:6] + m
            return m1
        elif (new[2:7] == list(range(x2,x2+5))):
            m = [8]
            m1 = new4[2:7] + m
            return m1
        else:
            return four_7(H)
    else:
        return four_7(H)



def four_7(H):
    '''Return a list of 4 cards with the same rank,
       if 4 of the 7 cards have the same rank in H, a list of 7 cards, 
       False otherwise.'''
    newA = []
    new2 = []
    new3 = []
    new4 = []
    new5 = []
    new6 = []
    new7 = []
    new8 = []
    new9 = []
    new10 = []
    new11 = []
    new12 = []
    new13 = []  
    for i in H:
        if i.get_rank() == 1:
            newA.append(i)
        elif i.get_rank()==2:
            new2.append(i)
        elif i.get_rank() == 3:
            new3.append(i)
        elif i.get_rank() == 4:
            new4.append(i)
        elif i.get_rank()==5:
            new5.append(i)
        elif i.get_rank() == 6:
            new6.append(i)
        elif i.get_rank() == 7:
            new7.append(i)
        elif i.get_rank()==8:
            new8.append(i)
        elif i.get_rank() == 9:
            new9.append(i)
        elif i.get_rank() == 10:
            new10.append(i)
        elif i.get_rank()==11:
            new11.append(i)
        elif i.get_rank() == 12:
            new12.append(i)
        elif i.get_rank() == 13:
            new13.append(i)    

    if len(newA) == 4:
        x = [7]
        newa = newA + x
        return newa
    elif len(new2) == 4:
        x = [7]
        newa = new2 + x
        return newa
    elif len(new3) == 4:
        x = [7]
        newa = new3 + x
        return newa
    elif len(new4) == 4:
        x = [7]
        newa = new4 + x
        return newa
    elif len(new5) == 4:
        x = [7]
        newa = new5 + x
        return newa
    elif len(new6) == 4:
        x = [7]
        newa = new6 + x
        return newa
    elif len(new7) == 4:
        x = [7]
        newa = new7 + x
        return newa
    elif len(new8) == 4:
        x = [7]
        newa = new8 + x
        return newa
    elif len(new9) == 4:
        x = [7]
        newa = new9 + x
        return newa
    elif len(new10) == 4:
        x = [7]
        newa = new10 + x
        return newa
    elif len(new11) == 4:
        x = [7]
        newa = new11 + x
        return newa
    elif len(new12) == 4:
        x = [7]
        newa = new12 + x
        return newa
    elif len(new13) == 4:
        x = [7]
        newa = new13 + x
        return newa
    else:
        return full_house_7(H)

def full_house_7(H):
    '''Return a list of 5 cards forming a full house,
       if 5 of the 7 cards form a full house in H, a list of 7 cards, 
       False otherwise.'''
    
    newA = []
    new2 = []
    new3 = []
    new4 = []
    new5 = []
    new6 = []
    new7 = []
    new8 = []
    new9 = []
    new10 = []
    new11 = []
    new12 = []
    new13 = []  
    for i in H:
        if i.get_rank() == 1:
            newA.append(i)
        elif i.get_rank()==2:
            new2.append(i)
        elif i.get_rank() == 3:
            new3.append(i)
        elif i.get_rank() == 4:
            new4.append(i)
        elif i.get_rank()==5:
            new5.append(i)
        elif i.get_rank() == 6:
            new6.append(i)
        elif i.get_rank() == 7:
            new7.append(i)
        elif i.get_rank()==8:
            new8.append(i)
        elif i.get_rank() == 9:
            new9.append(i)
        elif i.get_rank() == 10:
            new10.append(i)
        elif i.get_rank()==11:
            new11.append(i)
        elif i.get_rank() == 12:
            new12.append(i)
        elif i.get_rank() == 13:
            new13.append(i)    

    f = []
    if len(newA) >= 2:
        f += newA
    if len(new2) >= 2:
        f += new2
    if len(new3) >= 2:
        f += new3
    if len(new4) >= 2:
        f += new4
    if len(new5) >= 2:
        f += new5
    if len(new6) >= 2:
        f += new6
    if len(new7) >= 2:
        f += new7
    if len(new8) >= 2:
        f += new8
    if len(new9) == 2:
        f += new9
    if len(new10) == 2:
        f += new10
    if len(new11) == 2:
        f += new11
    if len(new12) == 2:
        f += new12
    if len(new13) == 2:
        f += new13
    if len(f) == 5:
        x = [6]
        f += x
        return f
    else:
        return flush_7(H)


def flush_7(H):
    '''Return a list of 5 cards forming a flush,
       if at least 5 of 7 cards form a flush in H, a list of 7 cards, 
       False otherwise.'''
    new1 = []
    new2 = []
    new3 = []
    new4 = []
    for i in H:
        if i.get_suit() == 1:
            new1.append(i)
        elif  i.get_suit()==2:
            new2.append(i)
        elif i.get_suit() == 3:
            new3.append(i)
        elif i.get_suit() == 4:
            new4.append(i)
    if len(new1) >= 5:
        x= [5]
        new1 += x
        return new1
    elif len(new2) >= 5:
        x= [5]
        new2 += x
        return new2
    elif len(new3) >= 5:
        x= [5]
        new3 += x
        return new3
    elif len(new4) >= 5:
        x= [5]
        new4 += x
        return new4
    else:
        return straight_7(H)

def straight_7(H):
    '''Return a list of 5 cards forming a straight,
       if at least 5 of 7 cards form a straight in H, a list of 7 cards, 
       False otherwise.'''
    new = []
    for i in H:
        i = i.get_rank()
        new.append(i)
    final_list = []
    for num in new:
        if num not in final_list: 
            final_list.append(num)
    x = final_list[0]
    x1 = final_list[1]
    x2 = final_list[2]
    if final_list[:5] == list(range(x,x+5)):
        k= H[:5]
        k1 = [4]
        k += k1
        return k
    elif final_list[1:6] == list(range(x1,x1+5)):
        k= H[1:6]
        k1 = [4]
        k += k1
        return k
    elif final_list[2:7] == list(range(x2,x2+5)):
        k= H[2:7]
        k1 = [4]
        k += k1
        return k
    else:
        return three_7(H)
    
       
              

def three_7(H):
    '''Return a list of 3 cards with the same rank,
       if 3 of the 7 cards have the same rank in H, a list of 7 cards, 
       False otherwise.
       You may assume that four_7(H) is False.'''
    newA = []
    new2 = []
    new3 = []
    new4 = []
    new5 = []
    new6 = []
    new7 = []
    new8 = []
    new9 = []
    new10 = []
    new11 = []
    new12 = []
    new13 = []  
    for i in H:
        if i.get_rank() == 1:
            newA.append(i)
        elif i.get_rank()==2:
            new2.append(i)
        elif i.get_rank() == 3:
            new3.append(i)
        elif i.get_rank() == 4:
            new4.append(i)
        elif i.get_rank()==5:
            new5.append(i)
        elif i.get_rank() == 6:
            new6.append(i)
        elif i.get_rank() == 7:
            new7.append(i)
        elif i.get_rank()==8:
            new8.append(i)
        elif i.get_rank() == 9:
            new9.append(i)
        elif i.get_rank() == 10:
            new10.append(i)
        elif i.get_rank()==11:
            new11.append(i)
        elif i.get_rank() == 12:
            new12.append(i)
        elif i.get_rank() == 13:
            new13.append(i)

    if len(newA) == 3:
        x=[3]
        newa= newA + x
        return newa
    elif len(new2) == 3:
        x=[3]
        newa= new2 + x
        return newa
    elif len(new3) == 3:
        x=[3]
        newa= new3 + x
        return newa
    elif len(new4) == 3:
        x=[3]
        newa= new4 + x
        return newa
    elif len(new5) == 3:
        x=[3]
        newa= new5 + x
        return newa
    elif len(new6) == 3:
        x=[3]
        newa= new6 + x
        return newa
    elif len(new7) == 3:
        x=[3]
        newa= new7 + x
        return newa
    elif len(new8) == 3:
        x=[3]
        newa= new8 + x
        return newa
    elif len(new9) == 3:
        x=[3]
        newa= new9 + x
        return newa
    elif len(new10) == 3:
        x=[3]
        newa= new10 + x
        return newa
    elif len(new11) == 3:
        x=[3]
        newa= new11 + x
        return newa
    elif len(new12) == 3:
        x=[3]
        newa= new12 + x
        return newa
    elif len(new13) == 3:
        x=[3]
        newa= new13 + x
        return newa
    else:
        return two_pair_7(H)
        
        
def two_pair_7(H):
    '''Return a list of 4 cards that form 2 pairs,
       if there exist two pairs in H, a list of 7 cards, 
       False otherwise.  
       You may assume that four_7(H) and three_7(H) are both False.'''
    newA = []
    new2 = []
    new3 = []
    new4 = []
    new5 = []
    new6 = []
    new7 = []
    new8 = []
    new9 = []
    new10 = []
    new11 = []
    new12 = []
    new13 = []  
    for i in H:
        if i.get_rank() == 1:
            newA.append(i)
        elif i.get_rank()==2:
            new2.append(i)
        elif i.get_rank() == 3:
            new3.append(i)
        elif i.get_rank() == 4:
            new4.append(i)
        elif i.get_rank()==5:
            new5.append(i)
        elif i.get_rank() == 6:
            new6.append(i)
        elif i.get_rank() == 7:
            new7.append(i)
        elif i.get_rank()==8:
            new8.append(i)
        elif i.get_rank() == 9:
            new9.append(i)
        elif i.get_rank() == 10:
            new10.append(i)
        elif i.get_rank()==11:
            new11.append(i)
        elif i.get_rank() == 12:
            new12.append(i)
        elif i.get_rank() == 13:
            new13.append(i)    
    final = []
    if len(newA) == 2:
         final += newA
    if len(new2) == 2:
         final += new2
    if len(new3) == 2:
         final += new3
    if len(new4) == 2:
         final += new4
    if len(new5) == 2:
         final += new5
    if len(new6) == 2:
         final += new6
    if len(new7) == 2:
         final += new7
    if len(new8) == 2:
         final += new8
    if len(new9) == 2:
         final += new9
    if len(new10) == 2:
         final += new10
    if len(new11) == 2:
         final += new11
    if len(new12) == 2:
         final += new12
    if len(new13) == 2:
         final += new13
    if len(final) >= 4:
        x=[2]
        final += x
        return final
    else:
        return one_pair_7(H)
        

def one_pair_7(H):
    '''Return a list of 2 cards that form a pair,
       if there exists exactly one pair in H, a list of 7 cards, 
       False otherwise.  
       You may assume that four_7(H), three_7(H) and two_pair(H) are False.'''
    
    newA = []
    new2 = []
    new3 = []
    new4 = []
    new5 = []
    new6 = []
    new7 = []
    new8 = []
    new9 = []
    new10 = []
    new11 = []
    new12 = []
    new13 = []  
    for i in H:
        if i.get_rank() == 1:
            newA.append(i)
        elif i.get_rank()==2:
            new2.append(i)
        elif i.get_rank() == 3:
            new3.append(i)
        elif i.get_rank() == 4:
            new4.append(i)
        elif i.get_rank()==5:
            new5.append(i)
        elif i.get_rank() == 6:
            new6.append(i)
        elif i.get_rank() == 7:
            new7.append(i)
        elif i.get_rank()==8:
            new8.append(i)
        elif i.get_rank() == 9:
            new9.append(i)
        elif i.get_rank() == 10:
            new10.append(i)
        elif i.get_rank()==11:
            new11.append(i)
        elif i.get_rank() == 12:
            new12.append(i)
        elif i.get_rank() == 13:
            new13.append(i)    

    if len(newA) == 2:
        x= [1]
        newa = newA + x
        return newa
    elif len(new2) == 2:
        x= [1]
        newa = new2 + x
        return newa
    elif len(new3) == 2:
        x= [1]
        newa = new3 + x
        return newa
    elif len(new4) == 2:
        x= [1]
        newa = new4 + x
        return newa
    elif len(new5) == 2:
        x= [1]
        newa = new5 + x
        return newa
    elif len(new6) == 2:
         x= [1]
         newa = new6 + x
         return newa
    elif len(new7) == 2:
        x= [1]
        newa = new7 + x
        return newa
    elif len(new8) == 2:
        
        x= [1]
        newa = new8 + x
        return newa
    elif len(new9) == 2:
        x= [1]
        newa = new9 + x
        return newa
    elif len(new10) == 2:
        x= [1]
        newa = new10 + x
        return newa
    elif len(new11) == 2:
        x= [1]
        newa = new11 + x
        return newa
    elif len(new12) == 2:
        x= [1]
        newa = new12 + x
        return newa
    elif len(new13) == 2:
        x= [1]
        newa = new13 + x
        return newa
    else:
        return high_Card(H)
   


def high_Card(H):
    """ reutrn the original cards of the player"""
    x = [0]
    m = H[:5] + x
    return m



def main():
    
    D = cards.Deck()
    n = D.cards_count()
    D.shuffle()
    while n>9:
        community_list = []
        for i in range(5):
            community_list.append(D.deal())
        hand_1_list = []
        hand_2_list = [] 
        for i in range(2):
            hand_1_list.append(D.deal())
            hand_2_list.append(D.deal())
        hand_1_list1 = community_list +hand_1_list
        hand_2_list2 = community_list + hand_2_list
        print("Community cards: ",community_list)
        print("Player 1 :", hand_1_list)
        print("Player 2 :",hand_2_list)
        
        slectionList1 = slection(hand_1_list1)
        slectionList2 = slection(hand_2_list2)
      
        order = straight_flush_7(slectionList1)

        x = order.pop()

        order1 = straight_flush_7(slectionList2)

        x1 = order1.pop()
        
        if x > x1:
            if x == 1:
                print("player 1 wins with one pair: ",order)
            elif x == 2:
                print("player 1 wins with two pairs: ",order)
            elif x == 3:
                print("player 1 wins with Three of a kind: ",order)
            elif x == 4:
                print("player 1 wins with Straight: ",order)
            elif x==5:
                print("player 1 wins with Flush: ",order)
            elif x==6:
                print("player 1 wins with Full house: ",order)
            elif x==7:
                print("player 1 wins with Four of a kind: ",order)
            elif x==8:
                print("player 1 wins with Straight flush: ",order)
        elif x1 > x:
            if x1 == 1:
                print("player 2 wins with one pair: ",order1)
            elif x1 == 2:
                print("player 2 wins with two pairs: ",order1)
            elif x1 == 3:
                print("player 2 wins with Three of a kind: ",order1)
            elif x1 == 4:
                print("player 2 wins with Straight: ",order1)
            elif x1 ==5:
                print("player 2 wins with Flush: ",order1)
            elif x1 ==6:
                print("player 2 wins with Full house: ",order1)
            elif x1 ==7:
                print("player 2 wins with Four of a kind: ",order1)
            elif x1 ==8:
                print("player 2 wins with Straight flush: ",order1)

        elif x == x1:
            if (x == 0) and (x1 == 0):
                print("TIE with high cards")
            elif (x == 1) and (x1 ==1) :
                print("TIE with one pair: ",order)
            elif (x == 2) and (x1 ==2):
                print("TIE with two pairs: ",order)
            elif (x == 3) and (x1 ==3):
                print("TIE with Three of a kind: ",order)
            elif (x == 4) and (x1 ==4):
                print("TIE with Straight: ",order)
            elif (x==5) and (x1 == 5):
                print("TIE with Flush: ",order)
            elif (x==6) and (x1 == 6):
                print("TIE with Full house: ",order)
            elif (x==7) and (x1 == 7):
                print("TIE with Four of a kind: ",order)
            elif (x==8) and (x1==8):
                print("TIE with Straight flush: ",order)


        
                
                
        n = D.cards_count()    
        

        if n > 9:
            other = input("Do you wish to play another hand?(Y or N)")
            
            if other == "Y"  or other == "y":
                n = D.cards_count() 
                print("----------------------------------------")
                print("Let's play poker!")
            else:
                print("----------------------------------------")
                print("Nice try,The game is done")
                sys.exit()
                
                
        else:
            print("Deck has too few cards so game is done.")

if __name__ == "__main__":
    main()
