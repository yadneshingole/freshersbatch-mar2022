#We need to create a menu for our users. Display a menu containing three choices AND a choice to allow them to #exit. Display that menu and prompt for a choice. Upon choosing the value, it should simply clear the screen and #redisplay the menu (loop until the exit choice is given).

#HOWEVER, we need to be sure that the end user cannot use CTL-C, CTL-Z or a KILL command to terminate the #application. Add a 'trap' in the script to capture those attempts and provide instructions on how to exit the #script using the menu choice instead.


echo "Start!"
echo "What you like to eat?"  
echo "Burger - press 1"
echo "Pizza - press 2"
echo "Fries - press 3"
echo "Exit - press 0"
read -p "1|2|3|0? :" Answer
until [[ $Answer -eq 0 ]]
do
case $Answer in  
    1)  
        echo "Burger it is"  
   read -p "1-Burger|2-Pizza|3-Fries|0-Exit? :" Answer 
        ;;  
    2)  
        echo "Oh it is Pizza"  
read -p "1-Burger|2-Pizza|3-Fries|0-Exit? :" Answer
        ;;   
        
    3)  
        echo "FRIES it is"  
     read -p "1-Burger|2-Pizza|3-Fries|0-Exit? :" Answer
        ;;
    0)  
        echo "exit..."  
        break;  
        ;;      
    *)
      echo "try with correct choice"
read -p "1-coffee|2-colddrink|3-beer|0-exit? :" Answer
        ;;
esac  
done
