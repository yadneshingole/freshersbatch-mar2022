#Write a script intended to iterate through an array called SERVERLIST containing at least four values (server #names). Display all four values to the terminal when run.

SERVERLIST=(1 2 3 4)

for i in ${SERVERLIST[*]}
do
	echo "Number is : $i"
done
