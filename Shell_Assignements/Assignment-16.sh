#Create a simple text file containing a list of super heros (or some names if preferred), use at least four #values, one per line in the file.

#Write a bash shell script that then reads that file and displays it line by line on the terminal window.

file='read_file.txt'  
  
i=1  
while read line; do  
  
#Reading each line  
echo "Line No. $i : $line"  
i=$((i+1))  
done < $file 

