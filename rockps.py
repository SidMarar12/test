import random 

s = ["rock", "paper", "scissors"] 
siddhant=False 
while (siddhant==False):
	siddhant=input("rock, paper or scissors?")
	computer1=s[random.randint(0,2)]
	print (siddhant)
	print (computer1)
	if (siddhant!="rock" and siddhant!="paper" and siddhant!="scissors"):
    		print("Not a valid response")
  	else:
    		if (siddhant==computer1):
      			print ("That's a tie! Let's go again.")
    		elif (siddhant=="rock" and computer1=="scissors"):
      			print ("Siddhant wins")
    		elif (siddhant=="paper" and computer1=="rock"):
      			print ("Siddhant wins")
    		elif (siddhant=="scissors" and computer1=="paper"):
      			print ("Siddhant wins")
    		else:
      			print ("Computer1 wins")
    		again=input("Play again?")
    		if (again=="yes"):
      			siddhant=False
    		elif (again=="no"):
      			print("Good game.")
    		else:
      			print ("Invalid response.")
      		siddhant=False
