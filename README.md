# Language-Matching-Pygame

# Overview

The code in this repository is for an english/spanish matching game.  It has a random selection of 12 english words and their 12 matching spanish counterparts
selected from a pool of 40 words each.  From there, the game launches the words at different velocities in different directions.  The goal of the game
is to click on a ward, and have the next click be on the equivalent word of the other language.  When the match is correct, the words disappear. If the match
is not correct, then the words stay the in the field.

Other things are in there for asthetic purposes such as music, backgrounds, colors, delay effects, studying the words, and keeping track of as well as displaying the
top 10 high scores and corresponding names/initials.

One important detail is that the pygameMenu.py file needs to be the file run for the game to launch.

# Development Environment

For this assignment, we used Visual Studio Code, python, pygame, and pygame_gui. We also used Google Firebase to keep track of the high scores.

# Collaborators

* Matt Loumeau
* Jared Denning
* Denis Lazo
* Jesse Fryar

# Useful Websites

* [PyGame](https://www.pygame.org/news)
* [FireBase](https://firebase.google.com/)

# Future Work

* We would like to create better backgrounds for the study words and high scores screens.
* It would be cool to implement large files of english/spanish matches.
* If we incorporate large files, then the audio for each word will be much harder to account for (in the study words section).
