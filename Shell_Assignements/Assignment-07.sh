#Write a script that will use command substitution to dynamically set variable values:

#TODAYSDATE - should contain date/time stamp when executed
#USERFILES - the results of a find run on the /home directory to list all files owned by 'user' account


#Additionally, set two aliases:

#TODAY - should be an alias for the 'date' command
#UFILES - should be an alias to the full command used to set the variable USERFILES above

#Finally, display all variables and alias values when the script is run.

TODAYSDATE="date"
USERFILES="find"

alias TODAYSDATE="TODAY"
alias USERFILES="UFILES"
