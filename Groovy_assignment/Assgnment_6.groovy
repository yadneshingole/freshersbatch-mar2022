class Money {
    private String currency;
    private double amount;

    Money(String currency, double amount) {
        this.currency = currency
        this.amount = amount
    }

   def plus(Money other) {      // Plus Method overloading

        if(this.currency==other.currency){
            return new Money(this.currency,this.amount+other.amount)
        }
   }
    def minus(Money other) {        // Minus Method Overloadings

        if(this.currency==other.currency){
            return new Money(this.currency,this.amount-other.amount)
    } 
        

        
    }

    @Override                           //OVerride the operators
    public String toString() {
        return "Money{" +
                "currency='" + currency + '\'' +
                ", amount=" + amount +
                '}';
    }
}

def Money1 = new Money("euro", 500)
def Money2 = new Money("euro", 350)
def Money3 = Money1 + Money2
def Money4 = Money1 - Money2
println Money3
println Money4