class Prime{

    static boolean isPrime(int value){
        if (value<=1){
            println("Invalid input: "+value)
            return false;
            //println("Invalid")
        }
        for (int i=2; i<value;i++){
            if (value%i==0){
                println("$value is not a Prime Number")
                return false;
            }
        println("$value a Prime Number")
        return true;
        }
     
    }
    def printfun(){
        println ("Now we have checked the prime numbers for all the cases")
    }
  

// Main Function
static void main(args){
    Prime s= new Prime();
    s.isPrime(1);       // Gives Invalid Ouput
    s.isPrime(11);      // Gives Prime Ouput
    s.isPrime(22);      // Gives Not Prime Ouput
    s.printfun();  
    

}
}