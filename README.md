# messengerExtract
Goal is to use Messenger's search function and screenshot EVERY instance of a searched word. 

## Basic Functionality
* Simple GUI appears, enter Username, Email, Conversation, and SearchKey you want to search up
* Bot will then go through all instances that was searched up and screenshot each instance so that you may look through it later.
* Result will be a folder of images containing the key word you want. 

## Possible Advanced Functionality
* Allows user to browse through results using GUI, then choose to discard or save them (select ones?)
* Save the whole conversation from beginning to end (Perhaps another project)
* If no Conversation is specified than all Conversations will be searched
* Image Compare: prevent overlapping screenshots by comparing the images to one another, can also be done during the scrape to "speed" up the process (i.e., if a similar image or images are found than cease the scrape (since it's chronological)).

## How to Install
## How to Run
Windows - Python gui.py
## Resources Used
* Selenium - Web Scraping tool used to go to Messenger and take screenshots of conversation 
* PyQT5 - Used to generate simple GUI
