# kotlin-win-ui44oig4p98

Numbers

```Kotlin
val fish = 2
fish.times(2) //output 4
.plus
.div
.minus
Fish.ToInt / .toLong()
```

```Kotlin
var = dim
val = const
object warpper: val boxed: Number = 1
fun ___(){}
No ;
Println(“guhgivswoify”)
```

```Kotlin
Dim as as string //null
String as; //null
Kotlin: var as : Int? = null
var as: List<String>? = listOf(nuill. null)
var as: List<String>? = null
as!!.eat()

! = bang !!= double bang (what is it(not null
```

Null Exception @Kotlin

```Kotlin
//check whether var is not null

var num = 5
Num?.dec() ?: 0 //if num not null, use num as return, otherwise return 0
?: //elvis operator

"He has ${ a + b} cows - $a"

 == != //comparison

<> //SQL not

if (num in 1..100) do // if number in 1- 100 range

when (input){ //select case
in 0..100 -> println  //auto break
101 -> println
else -> println
}
when{happy == 100 -> “happy”}
```

Array amd List

```Kotlin
val myList  =mutableListOf(“”,””,””) //reference
myList = mutableListOf(“”,””) //error
myList.remove(“”) // fine //true
ListOf(5,12) //collection
val variable = arrayOf(“hi”, 73254672) //unspecified type
val intArray = intArrayOf(1,2,3)
Println(Arrays.ToString(variable))  //to print => string

val nestArray = arrayOf(variable, intArray)
val array = Array(6){it *2} //array size, it = array index (from 0 , +=1)
println(array.asList())  //[0, 2, 4, 6, 8, 10]

for(element in arrayvariable) //for each
for((index,element) in array.withIndex()){} //built-in index function
for (i in ‘b’… ‘d’){println(i)} // bcd (range in alphabet)
for(i in 5 downTo 1 step 2) // 54321 (downTo = step -1)
array[5]

100.mod(7) //2
```

Function

```Kotlin
fun main(){} // 
// every function return value   
// return "type unit" == no value

fun main(args: Array<String>){} // Array<String> can be set in Run> Edit Configuration> Program Argu
_println_("Hello ${args[0]}!")
args[0] //applied to nodejs , good

val isUnit = println(“hi”)
println(isUnit) //return Kotlin.Unit
val isHot = if(temp ==20) true else false //false

fun randomd() : String{} // return a string value
fun swim(speed: String = “fast”){} //parameter default fast
swim(speed = “slow”)
```

kotlin style variable declaration

```Kotlin
fun getPair() = Pair(1, "foo")
fun num() = 20
fun isTooHot(temp :Int)  = temp> 20
```

slow your app and potential out-of-memory errors

```Kotlin
fun make() = println(“”)
fun makenew( var :Any = make()) {} //if no parameter passed, whole var is made as default ==make()

Repeat(2){} //kotlin library (same as for loop)
```

Cannot assign for/while in variable

```Kotlin
val variable = for(x in 1..2){}
val variable= while(){}
```

//kotlin (not interchangable)and C# ‘    ’ for char “   ” for string

```Kotlin

filter == indexOf() // contains
val variable = listOf(“hey”, “heyman”, “on9”)`
val list_that_only_have_h = variable.filter{ it[0]} == ‘h’}  //it[0] == first character // [hey, heyman] //printable, eager?
val filter_lazily = variable.asSequence().filter{ it[0]} == ‘h’} //how API works
Println(filter_lazily.toList())
val lazy_map = variable.asSequence().map { println (it) } // output: hey
Println(lazy_map.first()) //output:hey
Println(lazy_map.toList()) // [“hey”, “heyman”, “on9”]
```

Lambda

```Kotlin
fun ___(){}  //named function
{ code of lines }()       //Lambda //anonymus function or function literals ///high-order function
val swim = { print(swim) }       swim() //lambda
val lambdafunction = { variable :String -> code of lines} //lambda parameters
val lambdafunc : (Int) -> Int = {parameter -> return} //lamda only data type

fun function1( variable :Int ) = variable +10
fun update(dirty :Int , lambdavariable :(Int) -> Int): Int{ return lambdavariable(dirty) }
var dirty = 20
Dirty = update(dirty, lambdafunc) //parameter Int, lambda
Dirty = update(dirty, ::function1 ) // ::function1 is not call function but parse a reference as lambda
Dirty = update(dirty) { dirty -> dirty +50 } //exactly use lambda behind lol

val random1 = random()  //value assign at compile (wont change runtime
val random2 = {random()} //every time call, execute (as reference)
```

classes !\[\[Pasted image 20230118121139.png]] !\[\[Pasted image 20230118121146.png]]

```Kotlin
class Something{
	val height = 50 //properties
	Get(){ return height}   or get() = height
	Public Set (value) { height = value * 2} //no one outside can access setter

	fun functionName = height
}

fun another(){ val variable = Something()  
	Println(“ ${variable.height} , ${variable. functionName}”) }

class something ( var/val parameter :Int  = “default value” ){       //var/val create properties
constructor( variable2 :Int) :this() {}  } //define constructor, calculation specific for constructor
val variable = something( variable2 = 89)
```

!\[\[Pasted image 20230118121207.png]]

most class only specify one constructor with default parameter //constructor overload not needed]

```Kotlin
class something( val number: Int){
	val variable :Int
	Init { when(number){ 0 -> 5
	In 1..3 -> 7}} //return5
	Constructor() : this ( 8 ) {}}           

class something () :Any {} // All class by default inheritance with Any
open class something() { //open is necessary for inheritance
open var variable = 50} // open is necessary for inheritance

class some2() : something(){  //inheritance by naming the data type as the class
override var variable = 60} //open is needed before override
```

Abstract

```Kotlin
some basic function, properties like: people head = 1

abstract class and interface => both cant instantiate object
abstract class has constructor logic but interface doesn’t
abstract class (with constructor) or Interfaces // both are class that cant instantiate their own = cannot create object
abstract class Name{ abstract val vaiable :Int }//create abstract class, abstract variable =something must have
class Name2 : Name () { override val variable = 7 } //make sure it contains in the class
```
