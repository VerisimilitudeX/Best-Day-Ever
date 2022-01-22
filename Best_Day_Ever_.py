"""
LESSON: 2.2 - Conditionals (Else)
EXERCISE: Best Day Ever
"""

#### ---- QUESTION 1---- ####

print("You wake up feeling great. Something tells you this day is going to be amazing!")
print("The first thing you do is try to get to school.")
print("Do you...")
print("  a) Miss the bus")
print("  b) Ride the bus")
print("  c) Get someone to drive me")
user_choice = input("Choose (a / b / c): ")
print()


#### ---- RE-STRUCTURE 1 ---- ####

# Change the IF conditionals below into a single
# conditional with IF and ELIF clauses
if user_choice == "a":
    print("You missed the bus. ...But your friend comes by just then.")
    print("It seems she's just invented a jetpack and wants you to test it!")
    print("You take a super awesome jetpack ride to school!")

elif user_choice == "b":
    print("You take the bus to school... or so you thought!")
    print("It turns out this bus is having a special morning field trip to the beach!")
    print("You spend a couple awesome hours just chilling in the sun and listening to the waves.")

elif user_choice == "c":
    print("You got someone to drive you to school.")
    print("On the way there, you can't help but notice the live velociraptor keeping pace with the car!")
    print("Luckily, it's friendly. It just wanted to say hey.")

# Add an ELSE-clause that handles incorrect input.
# Add your own version of what happens in that case.
# For example: You're not sure how you got to school.
#              You just closed your eyes and there you were.
#              You seem to have spontaneously developed the ability to teleport!
else:
    print("You seem to have spontaneously developed the ability to teleport!")
    print("You just closed your eyes and there you were.")
    print("You're not sure how you got to school.")



#### ---- QUESTION 2 ---- ####

print()
print("There's a quiz today. ...Did you study for it?")
print("  y) Of course I did!")
print("  n) ...Whoops, I forgot.")
user_choice = input("Choose (y / n): ")
print()


#### ---- RE-STRUCTURE 2 ---- ####

# Change these IF conditionals into a single
# conditional with IF and ELIF clauses
if user_choice == "y":
    print("You studied super hard and you aced the test!")
    print("Congrats, you got the highest score! All your friends got pretty good scores too.")

elif user_choice == "n":
    print("You forgot to study... but it turns out the quiz was cancelled!")
    print("The teacher decided you were way too smart for that quiz.")
    print("The class watches a movie instead.")

# Add an ELSE-clause for incorrect input.
# Add your own version of what happens in that case.
# For example: Well, did you study or didn't you?
#              The world shatters because of this paradox of indecision.
#              It re-forms into a world where you never had a scheduled quiz.
#              The class watches a movie instead.
else:
    print("The world shatters because of this paradox of indecision.")
    print("Well, did you study or didn't you?")
    print("It re-forms into a world where you never had a scheduled quiz.")
    print("The class watches a movie instead.")



#### ---- QUESTION 3 ---- ####
    
print()
print("What do you want to do after school?")
print("  a) Go play in the soccer game")
print("  b) Volunteer to help clean up down by the river")
print("  c) Hang out with friends at the park")
print("  d) Just go home")
user_choice = input("Choose (a / b / c / d): ")
print()


#### ---- RE-STRUCTURE 3 ---- ####

# Change these last IF conditionals into a single
# conditional with IF and ELIF clauses
if user_choice == "a":
    print("You totally rock that soccer game, scoring the game-winning goal deep in extra time!")
    print("A professional soccer recruiter notices you and is very impressed.")
    print("Maybe you can get some kind of endorsement deal out of this...")

elif user_choice == "b":
    print("You do a good deed and restore a natural environment to pristine condition.")
    print("Also you find some sweet pirate treasure hidden in an old pipe!")

elif user_choice == "c":
    print("When you get to the park, it turns out there's a carnival set up there for the day.")
    print("It turns out it's free, so you can ride all the rides and play all the games!")
    print("There's even a puppy parade! Adorable.")

elif user_choice == "d":
    print("It seems there's a marathon of your favorite show on TV this afternoon.")
    print("You don't have any homework, so you can watch the whole thing.")
    print("Sometimes the best days are when you just kick back and relax.")

# Add another ELSE-clause for incorrect input.
# Add your own version of what happens in that case.
# For example: You discover a crack in the fabric of space-time.
#              It seems you have strange reality-warping powers where you don't have to take the options offered to you.
#              You re-make the universe based on your own whims.
#              ...It turns out to be fairly similar to this one.
else:
    print("It seems you have strange reality-warping powers where you don't have to take the options offered to you.")
    print("You discover a crack in the fabric of space-time.")
    print("You re-make the universe based on your own whims.")
    print("...It turns out to be fairly similar to this one.")


#### ---- CONCLUSION ---- ####

print("In the end, this will truly go down in history as the most epic of days.")


# Turn in your Coding Exercise.