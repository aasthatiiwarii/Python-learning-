print("Hello World")
import pyjokes
joke = pyjokes.get_joke()
print(joke)
#this print a random joke #single line comment

"""
so thanks
that was my program
"""
# double line comment

#question
# write program to print twinkle twinkle little star poem using python


print( ''' Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.
Twinkle, twinkle, little star,
How I wonder what you are!

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.
Twinkle, twinkle, little star,
How I wonder what you are!

Then the traveller in the dark,
Thanks you for your tiny spark,
He could not see which way to go,
If you did not twinkle so.
Twinkle, twinkle, little star,
How I wonder what you are!

In the dark blue sky you keep,
And often through my curtains peep,
For you never shut your eye,
Till the sun is in the sky.
Twinkle, twinkle, little star,
How I wonder what you are!

As your bright and tiny spark,
Lights the traveller in the dark,—
Though I know not what you are,
Twinkle, twinkle, little star.
Twinkle, twinkle, little star,
How I wonder what you are!''')

#que 2
# use REPL and print the table of 5 using (5*1)
5*1
5*2
5*3
5*4
5*5
5*6
5*7
5*8
5*9
5*10

#QUE 3
#Install an external and use it to perform an operation of your interest

import pyttsx3
engine = pyttsx3.init()
engine.say("Aastha,you are beautiful!")
engine.runAndWait()

# write a python program to print the contents of a directory using the os module

import os

# Specify the directory you want to list
directory_path = '/new folder'

# List and print contents of the directory in the specified path

contents = os.listdir(directory_path)
    
# print each file and directory name 
for item in contents:
    print(item)

    # que 5 lable the program written in problem 4 with comments

