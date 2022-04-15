import java.util.Arrays;
class sort_string{

    public void main(String [] args){

        def list=["Yadnesh","Om","Shrehari","Megha","Sonali"]
        println("Original list $list")
        sorted_list=list.sort()
        println("Sorted list $sorted_list")

        len=list.sort{a,b ->a.length()<=> b.length ?: a <=> b}
        println(len)
    }
}
    
