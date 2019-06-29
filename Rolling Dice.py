import random
#help(random)
min=2
max= 7

play = True
while play:
 chance = input( " enter y to play, and Stop to End the Game: ")
 if chance =='y':
    roll= random.randint(min,max)
    print( "you rolled ", roll)
  
 else :
    play = False
    print( " You had Stopped the Game")

    
