#	warmer.py		3/11/96 by Joe Strout

import random		# handy random-number functions

def run():
	# pick a number in the range 1-100
	mynum = random.randint(0,100) #randint(0,100)
	#print mynum
	yourguess = 200		# what user guessed
	lastdist = 0		# last distance to mynum
	tries = 0			# number of tries so far

	print "I'm thinking of a number from 1 to 100."
	
	# main loop: repeat until user gets it right
	while yourguess != mynum:
	
		tries = tries + 1
		yourguess = input("Your guess? ")
	
		if (yourguess != mynum):
		
			# find how far off you are
			newdist = abs(yourguess - mynum)
	
			# print warmer/colder than last time
			if (lastdist == 0):
				print "Guess again..."
			elif (newdist > lastdist):
				print "You're getting colder."
			else:
				print "You're getting warmer."
			lastdist = newdist
			
		# end of the if statement
	# repeat until user gets it right
	
	print "Good job!  That took", tries, "tries."
run()
#print test
# immediate-mode commands, for drag-and-drop or execfile() execution
if __name__ == '__main__':
	run()
	print
	raw_input("press Return>")
else:
	print "Module warmer imported."
	print "To run, type: warmer.run()"
	print "To reload after changes to the source, type: reload(warmer)"

# end of warmer.py
