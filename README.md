# Conlang Creation

This repository contains all the files needed to assist in creating your own conlang.

At the moment, implemented features include a basic Dictionary, allowing words to be added and searched. Features are constantly being added, with the end goal of this being a one-stop resource for all your language-creation needs.

Part of the goal for this program is for it to be accessible to all; as such, early on I am doing everything possible to make everything run smoothly and intuitively even if you have no prior programming knowledge. Because of this, some things may look weird to those who know how these things typically work. This is intentional, as I have found through testing and communicating with non-programmers that these odd ways of managing things work better than more straightforward and efficient methods do at this stage of the program. Please note, as the front end  improves many of these odd backend methods will be changing too, as it will not be necessary for them to be easily managed or observed by those without programming knowledge. 

# How to Open the Dictionary
Prerequisites: SQLite

The file Hub.py will ultimately be in charge of everything the dictionary has to offer. While still in development, if you would like to test out some of the features you can simply run Hub.py and navigate to the address provided in the terminal. If you would like to start working with your own data, you can easily fork this repository, making sure to delete mydictionary.db in order to empty it out (No need to replace, the file will automatically be regenerated upon running the program).

Eventually, everything will be taken care of through Hub.py, or some similar file, allowing you to run it and control everything from the window.

# Using a Custom Script

For the time being, script creation is being outsourced to a third party (I recommend Fontstruct, but any program allowing for .ttf or .otf files should work). Simply create and download a font, then install it into your computer's font library in order to use it with this program. Default naming convention in use here is to name the file "Conlang". If named differently, you may need to find and replace the font name in the program. This will be made easier eventually, likely once the dictionary is fully functioning.

This goes especially for non-alphabet users, but if your conscript requires more than 26 base characters, I highly recommend using a program such as Ukelele for Mac or Microsoft Keyboard Layout Creator in order to accomodate more characters. Having worked with Ukelele, it is relatively easy to make use of more than 200 characters should you need to thanks to options for shift, alt/option, and capslock keys.

In the future, I do plan to have a native conscript creation tool available. However, this is likely to be implemented long into the future as it is a sizeable undertaking and, of all the goals of this program, it is the one most easily outsourced for now.

# Future Plans

In the near future, plans include:
* Central hub window for program
* Support for recording additional language features, such as Syntax, Semantics, and Culture
* Expanding support for example sentences
* Automatic IPA translations
* Resources for coming up with conlang ideas
* Data visualization for phoneme, syntax, and language analysis
* Improved storage options
* Reformatting of the repository

Long term, plans include:
* Options to create and store multiple conlangs, with abilities to compare and modify both
* Native control of custom scripts, with more support for logographies, abugidas, and other non-alphabets
* Improved support for importing your own language and script
* Make everything look nice, front end improvements
* Support for creating a teaching-system for your language

