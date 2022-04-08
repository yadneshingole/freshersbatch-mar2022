#Write a script that will prompt the user to enter a number between 1 and 3. Capture that number in a variable and #then test that variable. Be sure to display the variable and it's value as appropriate within an if/then/else #statement where the final statement will display if they did not enter a number between 1 and 3 telling them they #failed to follow instructions. Redirect errors from each of the tests to /dev/null (to prevent script errors from #showing if text is entered for example).

echo "Enter the value between 1 to 3"
read response
echo "Your response is:$response"

if [[ $response -eq 1 ]]
then  
	echo "Success"
elif [[ $response -eq 2 ]]
then
	echo "Success"

elif [[ $response -eq 3 ]]
then 	echo "Sucess"
else
	echo "Failed to follow instructions"
fi
