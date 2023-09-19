# Conlang Creation

This repository contains all the files needed to assist in creating your own conlang.

At the moment, implemented features include a basic Dictionary with the ability to type 
in your own custom script. Features are constantly being added, with the end goal of this
being a one-stop resource for all your language-creation needs.

Part of the goal for this program is for it to be accessible to all; as such, early on I
am doing everything possible to make everything run smoothly and intuitively even if you
have no prior programming knowledge. Because of this, some things may look weird to those
who know how these things typically work. This is intentional, as I have found through testing 
and communicating with non-programmers that these odd ways of managing things work better than more 
straightforward and efficient methods do at this stage of the program. Please note, as the front end 
improves many of these odd backend methods will be changing too, as it will not be necessary for them
to be easily managed or observed by those without programming knowledge. 

# How to Open the Dictionary
Prerequisites: Pygame

Make sure prereqs are installed and the repository forked, then open Dictionary.py and type the following commands into the terminal:

      python3
      from Dictionary import *

This should open up the dictionary. Commands can be run through the terminal, creating
a popup window where you can type in the custom script.

# Using a Custom Script

For the time being, script creation is being outsourced to a third party (I recommend Fontstruct,
but any program allowing for .ttf or .otf files should work). Simply create and download a font, then install
it into your computer's font library in order to use it with this program. Default naming convention
in use here is to name the file "Conlang"; this should work as-is for MacOS, and the Windows change to
"Conlang Regular" is also accounted for. If named differently, open GUI.py to find and replace the font name
in the program.

Additionally, when creating a font check what characters you are replacing. This program by default
uses unicode values starting with 0180, with support currently through 01EB. If using different
characters these values can easily be changed, again within GUI.py.

# Future Plans

In the near future, plans include adding:
* Support for recording additional language features, such as Syntax, Semantics, and Culture
* Expanding support for example sentences
* Automatic IPA translations
* Resources for coming up with conlang ideas
* Data visualization for phoneme, syntax, and language analysis
* Improved storage options
* Reformatting of the repository

Long term, plans include:
* Changing storage from a binary file to a more structured database
* Options to create and store multiple conlangs, with abilities to compare and modify both
* Central hub window for program, moving away from terminal-input
* Native control of custom scripts, with more support for logographies, abugidas, and other non-alphabets
* Improved support for importing your own language and script
* Make everything look nice, front end improvements
* Support for creating a teaching-system for your language

