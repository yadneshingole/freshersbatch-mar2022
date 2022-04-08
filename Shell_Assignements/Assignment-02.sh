#Write a script that sets FOUR variables:

#MYUSERNAME
#MYPASSWORD
#STARTOFSCRIPT
#ENDOFSCRIPT

#Populate the first two with some default value and use command redirection to set the third and fourth value to #the date/time of when the script was started and completed. Within the script, be sure to display the values to #the terminal when run.

#!/bin/bash
MYUSERNAME="username"
MYPASSWORD="password123"
STARTOFSCRIPT=`date`echo "My login name for this application is: $MYUSERNAME"
echo "My login password for this application is: $MYPASSWORD"
echo "I started this script at: $STARTOFSCRIPT"
ENDOFSCRIPT=`date`
echo "I ended this script at: $ENDOFSCRIPT"
