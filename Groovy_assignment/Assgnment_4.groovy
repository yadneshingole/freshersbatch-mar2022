def lst=[1,2,3,4,5]
def sum=0
for (int i in lst){
    sum=sum+i

}
println("Original List $lst")
println("\nAddition of number in list is $sum")

def count=0
println("Doubling each number in list:")
def lst2=[]             // DEFINING NEW LIST
for (int i in lst){
    count=i*2;
    lst2.add(count);
}
println(lst2)
println("Addition of number in new list: ")
def result=0
for (int i in lst2){
    result=result+i;

}
println(result)
len=lst2.size()
avg=result/len
println("Average of the new list is $avg")

