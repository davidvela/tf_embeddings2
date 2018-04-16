@echo test

GOTO EndComment2
This line is comment.
And so is this line.
And this one...
:EndComment0

python scr1.py & 
python scr2.py &
:EndComment1

start cmd /k echo Hello, World1!
start cmd /k echo Hello, World2!

:EndComment2

start cmd /k python scr1.py
start cmd /k python scr2.py

:EndComment3
