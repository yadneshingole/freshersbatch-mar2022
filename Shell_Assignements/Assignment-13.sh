#Write a script that assigns a variable that contains a list of all shell scripts (*.sh) in the current directory

#(command redirection). Using the 'for'statement from the course, iterate through that list of files and display #the filename of each and cat out the contents to the terminal.

files=find . -name "*.sh"

