class Example {
   static void main(String[] args) {
      String a = "Hello, World. How are you?";
      String[] str;
      str = a.split(' ');   // split the sentence using blank space
      def s=str.size();
      def last=s-1;              
      last=str[last]            // stores the last word
      println(last.reverse())         // Prints the last word you as ?uoy
 
        

      
   } 
}