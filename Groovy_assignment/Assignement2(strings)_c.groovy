class Palindrome{


    static boolean isPalindrome(String str)
    {
 
        // Variables pointing to the beginning
        // and the end of the string
        int i = 0, j = str.length() - 1;
 
        
        while (i < j) {
 
            // if characters don't match
            if (str.charAt(i) != str.charAt(j))
                return false;
 
            // Increment first pointer and
            // decrement the other
            i++;
            j--;
        }
 
        // Given string is a palindrome
        return true;
    }
public static void main(String[] args)
    {
        // Input string
        String str = "racecar";
        String str1= "Bob"
        //Convert the string to lowercase
        str = str.toLowerCase();
        str1 = str1.toLowerCase();
    
        // passing bool function till holding true
        if (isPalindrome(str))
 
            // It is a palindrome
            System.out.print("Yes");
        
        else
 
            // Not a palindrome
            System.out.print("No");
        
        if(str1=='bob')
            print ("\nBob string is also palindrome after converting to lowercase")
    }
}