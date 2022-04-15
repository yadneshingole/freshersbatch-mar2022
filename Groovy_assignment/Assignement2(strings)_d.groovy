class Example {
   static void main(String[] args) {
      String a = "Hello, World. How are you?";
      String[] str;
      str = a.split(' ');   // split the sentence using blank space
      
      for( String values : str )
      println(values);
      println("Number of words are "+str.size())

        // Using Tokenize method which return array of list
      def resultList = a.tokenize()
      println("\nUsing Tokenize method to split the string")
      println(resultList)
        

      
   } 
}