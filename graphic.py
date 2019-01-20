from pyswip import *
import easygui
import random

# Creating a positive and negative expression list that will be used at random based on input to make the robot human like.

posReaction = ['Good boy!','Wow','Nice!','Makes sense.','Cool']

negReaction = ['Really?','Its fine','Oh!','Well its in the past now.']

#defining a default query structure/template to use everytime in the if else loops below.

#For the first question/ Random new Question
def query(initial, expression1):
        # Using easygui library/module to make a simple gui application to gather input in yes no format
	return easygui.ynbox('{} Was there {} today'.format(expression1, initial), '', ('Yes', 'No'))

#For the followup question.
def followUp(initial):
	#Using easygui library/module to make a simple gui application to gather input in yes no format
	return easygui.ynbox('Did you {}?'.format(initial), '', ('Yes', 'No'))


# This is the main logic that makes use of the previous defined templates and prolog database.
def main():
        
    # Found this defaut initialization on google and also the code to consult prolog file.
	prolog = Prolog()
	prolog.consult("logic.pl")
	
	# Need to start with some topic as everything is empty now.
	initial = 'playground'

	# This is the counter that keeps track if all the options have been asked or not.
	counter = False

	# Checks if this is the first time the program is being run.
	first = True
	pos = True

	# logic program loop
	while not counter:

		if first:
            # If this is the first time ask the default question and turn first to false so we dont get stuck in this loop.
			first = False
			answer = query(initial, 'Welcome back!')
			
		else:
			if positive:
                # Ask the question with a random positive starting emotional response.
				answer = query(initial, random.choice(posReaction))
			else:
                # Ask the question with a random negative starting emotional response.
				answer = query(initial, random.choice(negReaction))
		if answer:
			# Only ask a followup question if the child actually enjoyed doing the previous activity.
			followup = list(prolog.query('followup({}, Y)'.format(initial)))
			# There can be multiple followup like for build,draw,alphabet,hideandseek etc.
			followupRand = random.choice(followup)['Y']
			followupPos = followUp(followupRand)
			
			# IF they like the followup we add that to the like list too keep track and not repeat.
                        if followupPos:
                                prolog.assertz('like({})'.format(initial))
				positive = True 
			else:
				prolog.assertz('dislike({})'.format(initial))
				positive = False

		else:
			# Default to dislike if they didnt take part in the activity as we assume they didnt like it
			prolog.assertz('dislike({})'.format(initial))
			positive = False
                # Keep a track of what has been asked
		prolog.assertz('history({})'.format(initial))
		
		queryResult = list(prolog.query('ask(X, {})'.format(initial)))
		# Prolog function to find the length
		if len(queryResult) == 0:
                        # Length reaches 0 means no more data left
			end=easygui.ynbox('So overall was it a fun day!')
			if end:
                           easygui.msgbox('Nice now have some rest you did good!')
                        else:
                           easygui.msgbox('Aw its ok baby lets go shopping and eat Ice Cream!')    
			counter = True
			break
		initial = queryResult[0]['X']


# Indent it back to the left to end the main
if __name__ == "__main__":
	main()
