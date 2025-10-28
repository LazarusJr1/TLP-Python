palavra = ("secret")
guesses = ''
turns = 10

while turns > 0:         

    failed = 0                
    for char in palavra:      
        if char in guesses:    
            print (char,end=""),    
        else:

            print ("_",end=""),     
            failed += 1    
    if failed == 0:        
        print ("You won")
        break            

    guess = input("input a character:") 
    guesses += guess       

    if guess not in palavra:  
        turns -= 1        
        print ("Wrong")  
        print ("You have", + turns, 'more guesses' )
        if turns == 0:           
            print ("You Lose")