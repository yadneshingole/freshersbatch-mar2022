class course{
    String name;
    int days;

    static void main(String [] args){
        
        course first =  new course();    // first instance
        first.name="First"
        first.days=24

        course second = new course();    // second instance
        second.name="Second"
        second.days=12

        course third = new course();    // third instance
        third.name="Third"
        third.days=6

        course fourth = new course();    // forth instance
        fourth.name="Fourth"
        fourth.days=6

        def lst=[first.days,second.days,third.days,fourth.days]
        println(lst)
        def newlst = lst.sort(); 
        println("Sorted list $newlst")




    }
}