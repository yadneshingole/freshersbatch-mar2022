#Develop a simple three item menu to display on the terminal. Your script, upon display of the menu, should prompt #the user to choose one of the three available options. Using the 'case' statement from the course, display three #unique messages depending on which number they chose, with a catch all message letting them know if they went #outside the bounds of instructions.

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
