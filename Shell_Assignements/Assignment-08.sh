#Create a script that interacts with the user. You will want to prompt the user to enter the following information #(which you will capture and place into the following variables):

#FIRSTNAME
#LASTNAME
#USERAGE

#Greet the user with their name and current age displayed and then calculate and display their age in 10 years.

echo "Enter the first name"
read response
echo "You entered:$response"

echo "Enter the last name"
read response2
echo "You entered:$response2"

echo "Enter the age"
read response3
echo "You entered:$response3"

age10=$(($response3 + 10))

echo "Congrats your name is $response $response2 and your current age is $response3 and your age after 10 years is $age10."

