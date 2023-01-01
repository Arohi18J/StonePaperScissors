import random

def gamewin(comp,you):
    
    if comp==you:
        return None
    elif comp=='s':
   
        if you=='p':
            return False
        
        elif you=='sc':
            return True
        
        elif comp=='p':
   
            if you=='sc':
                return False
        
            elif you=='s':
                return True
        
        elif comp=='sc':
   
            if you=='s':
                return False
        
        elif you=='p':
            return True
        
print("comp turn:stone(s),paper(p) or Scissors(sc)?")
randNo=random.randint(1,3)
if randNo==1:
        comp='s'
        
elif randNo==2:  
        comp='p'
        
        
elif randNo==3:
        comp='sc'
        
        
        
you= input("Player1 turn: Stone(s),Paper(p) or Scissors(sc)?")
a=gamewin(comp,you)
if a ==  None:  
    print("The game is a tie")

elif a:
    print("You win!")
    
else :
    print("You lose")
