# paper 1

## Paper 1

obsidian

one note

notebook

goodnote

onedrive

problem solving question - sodu or murder mystery

## Basic

*   Variable

    giving a meaningful names to subroutines, function, variable.
*   constant vs Variable

    improve readability of code, easier to understand how it is used

    Easier to update code if change needed

    Assign VS editable @runtime
*   Global variable

    defined outside any procedure in scope of whole program
*   parameter

    information pass to/form a function or procedure, to define the value it is to use

    value passed into or out of procedure from/to calling program
*   benefit of parameters

    structure programming, local variable of subroutine\\

    scope: test independently

    enable same function to be used in a number of context, enable ‘black-box’ programming
*   parameter rather than global variable

    save memory since parameter take no space when not in use

    enable blackbox programming. portability of procedure

    Enable re-use of variable/ use variable without interfering other procedure
*   how data is share between sub-routine

    parameter

    value returned

    constant / global variable
*   Array msg\[50]

    data is stored in a series of contiguous/ consecutive memory location
* Algorithm Design
  * Sequence
  * Selection
  * iteration
  * assignment

💡 Describe how it doing, talk line by line, the background idea and the result?

*   Error

    Error handling: dealing with the event that cause current subroutine to stop

    * Invalid data type
    * Overflow ( too large/ memory insufficient
    *   Runtime error

        cause the program to stop

        Overwrite and out of range error - too long
    * Syntax error
    * Transcription
    * Logic

    Validation
*   Trace table

    all available, line by line
*   algorithm why is not working

    incorrect input due to error .
*   Structured Programming

| Structured English   | Pseudo code                | Structural Chart -sub-routine- | Flowchart      |
| -------------------- | -------------------------- | ------------------------------ | -------------- |
| Begin with Verb      |                            | From Left to Right             | Start/Stop     |
| INPUT READ           |                            | Level 0, 1, 2                  | Input/ Output  |
| MULTIPLY             | x == True :: :=            | Level 0 main program           | Process        |
| OUTPUT               | OUTPUT                     | import data                    | Printed Output |
| SET x to 40          | Assign x <- 40             | export data                    | Connector      |
| FOR EACH DO          | IF x in \[0,1,2] THEN ELSE | import & export data           | Decision       |
| LOOP DO              | For… END For               | main decision                  | Disk           |
| REPEAT UNTIL         | While… EndWhile            | Repeat                         | Tape           |
| SELECT VALUE x 1: 2: | Case x Of 1: EndCase       |                                |                |
| DO WHILE             |                            |                                |                |
*   Theory of computation

    Knowledgr: breaking problem into smaller sub-problem

    Understanding: each of which solve an identified task

    each of which might be further subdivided

    *   abstraction

| Representational           | by removing unnecessary details                  |     |
| -------------------------- | ------------------------------------------------ | --- |
| Procedural                 | broken down into procedure/ sub-routine design   |     | 
| Generalization             | grouping by common characteristics               |     |
| Functional                 | Broken down in to reusable function              |     |
| Data                       | organizing structure data/ hiding (using Classes |     |
| Problem                    | reducing problem                                 |     |
| remove unnecessary problem |                                                  |     |
    *   problem solving

        finding solution to real life problem
    * Information hiding VS Encapsulation
      *   information hiding

          only access or modified within object (access though derived method only

          hide all detail of an object that dont contribute to the essential characteristics
      *   Encapsulation SETTER and GETTER

          abstract data type (can change data type
    *   Decomposition

        break down problem into small piece
    *   Composition

        combining procedure into compound procedure
    *   Automation

        model are put into action to solve problem
*   Recursive algorithm

    sub-routine is call itself

    1. General case: include recursive call
    2. Base case include when condition met, routine will not call
    3. routine must call itself
    4. stopping condition must be reached after a finite number of call

    why stack?

    * the current state of the machine must be saved so can return to previous invocation of B
    * return address needed to be saved return correctly to previous

    Comparison to iteration

    * loop terminated vs base case
    * produce progressively
    * expensive method call ( copy of whole method
*   OOP

| class                       | template, !execute                     |
    | --------------------------- | -------------------------------------- |
    | object                      | instance of class, execute()           |
    | instantiation               | creating object from class             |
    | encapsulation               | grouping data, method in same gp       |
    | SETTER GETTER → constructor |                                        |
    | inheritance                 |                                        |
    | aggregation                 | <> has-a                               |
    | composition                 | \</> part-of                           |
    | polymorphism                | Inheritance                            |
    | overriding                  |                                        |
    | abstract                    | only signature, !implement             |
    | virtual                     | implement can redefine                 |
    | static                      | relevant to all instantance, no owning |
    | public                      | +                                      |
    | private                     | -                                      |
    | protected                   | #                                      |
*   Comment & code style

    good constrution. programmar friendly

## Sorting & Searching

*   Binary Search Tree

    Output sorted data

    rapidly/ fast searching of data

    organised into a logical structure when new data is added in
*   binary search condition

    sorted list. on the field being used as search key
* How binary search ork.
  1. Find the position of top and end of the list
  2. find out midpoint and median item, if founded return and exit
  3. If not, compare key field of record with median position.
  4. Decide on left, right and discard and repeat
  5. until either found or no further division possible. record doesn't exit.
*   Benefit binary search O(log2 n) over linear search O(n)

    IF linear at beginning, fast, at the end, slow

    Time complexity and eliminated half of the matches each time

    linear search search average n/2
*   Bubble Sort O(n^2) VS merge sort O(nlog n) Divide and Conquer

    hard to comprehend ( complex algorithm

    Recursive and memory size increase

    Efficient and quickness
*   How bubble sort work

    Switch when needed pair from top to end
*   How linear search algorithm work

    Search each element starting at the start until it find a match item
*   Traversal

    Tree: inorder preorder postorder

    | pre  | in   | post-order |
    | ---- | ---- | ---------- |
    | Root | L    | L          |
    | L    | Root | R          |
    | R    | R    | Root       |

    Graph: BFS, DFS

    * BFS: explore sibling before children
    * DFS: explore all children before sibling and pop out

## Data Type

*   dynamic data structure vs static

    Fix size → waste of storage

    Can change the data size → make sure no waste of memory

    more memory, store pointer next to them

    Easy to add /insert/shrink

    Move/ Adjust pointer only

    | Record      |   |
    | ----------- | - |
    | Array       |   |
    | Dictionary  |   |
    | #vector     |   |
    | Hash Table  |   |
    | Linked List |   |
*   What is heap and how it help with dynamic data structure

    heap is stored of all available/ free memory address
*   pointer

    hold the address for specific location of memory
*   Heap

    pool of unused memory

    for dynamic data type additional memory to store data
*   Linked List

    node: next node pointer + data

    sequential access

    * memory use
    * expansible
    * node operation easy
*   graph vs tree

    contains circle or cycle
*   weight graph

    has edge has a weight/value associated with it
*   adjacency list vs matrix

    list - when few edge between vertices //when in sparse

    when edge are rarely changed

    when the edge does not needed to be tested frequency

    > > save storage size
* Circular queue
* Uses of priority queue
*   Uses of stack

    store procedure call, local variable, parameter and return variable

    Reverse list. Push-in all content and pop out into new queue
*   How stack can use in advanced to reverse a queue

    Repeat S → Q until Q is empty

    Repeat Q→ S until S is empty

    Queue empified into Stack

    Element taken from front of queue push into stack

    Stack placed in queue
* \#vector
  1. Data Structure //list //array //dynamic //pointer
  2. Functions: mathematical construct map // f: S |→ R
  3. Geometric point in space (ARROW //head and tail
  4.  Vector addition (same dimension

      translate position of vector
  5.  Scalar-Vector Multiplication

      multiplying scalar by vector

      scalar \* vector
  6.  Convex combination

      combining 2 Vector. split(100%)

      40% \* vector 1 +60% \* vector 2
  7.  Dot Product

      a.b = (ax)(bx) + (ay)(by)

## Hash & Dictionary

*   Dictionary

    map key to data

    associative array deals with 2 set of data associated with each other

    * Add
    * retrieve
    * delete
*   Hash table

    data structure that store key/value pair based on an index calculated from an algorithm

    * Key - generated a hash value by hash function

    Collision handling method:

    collision occurs when two key compute same hash

    * Linear probing - algorithm probes and search for the next empty slot
    * Chaining - list is created in the slot and become element of list, next item
    * Rehashing - the process of running the hashing algorithm again when a collision occures
    * Larger hash table - each value in existing is inserted, position determined by new algorithm
*   Message digest/ checksum

    digest or checksum is simply a hash of the original message or file
*   hashing

    technique to convert a range of key value into a range of index of an array

    Process of applying hash function to generate hash value

    * security ( encryption
    * Fast storage, retrieval, searching and searching
    * Time efficiency O(1)

    Uses:

    * DB
    * Memory address
    * Encryption/ checksum
*   Hash function

    code that create a unique index from key data

    *   Clustering

        when hashing algorithm result are not randomly distributed → generate too much hash key around same value
*   MD5

    not-collision resistant ⇒ duplicate certificate

What is a model of simulation

## Maths & Algori

* Describe the language (w/ set of string
  1. Start with
  2. Followed by
  3. End with
*   State Transition Table

    Input, Current state, next state output

    First item with start state

    Last item Accept state’
*   Evaluate RPN

    Eliminate ()
*   Regex

    allow particular types of lang to describe in shorten notation

    simply a way of describing a set

    * File Searching
    * Matching
    * Finding word pattern
*   Regular language

    can be represented by a regex

    any language that a FSM will accept

    | \* | ≥ 0      |
    | -- | -------- |
    | +  | ≥ 1      |
    | ?  | optional |
    |    |          |
    | () | group    |
*   Set - no repeating data #set

    * finite set
    * infinite set
    * countably infinite - set of Natural number

 | Cartesian product | axb ≠ bxa (comma not reversible) |
    | ----------------- | -------------------------------- |
    | Cardinality       |                                  |

    set comprehension = the rule of the set

 | ∈  | member of (compare member) |
    | -- | -------------------------- |
    | ∉  | not a member of            |
    | ∪  | OR                         |
    | ∩  | AND                        |
    |  ø | NULL                       |
    | {} | a set                      |
    | ⊆  | subset of (compare set)    |
    | ⊂  | subset of and not equal    |
    | \\ | delete left from right     |

    {a,b,c} !∈ {a, b, c, d, e}
*   UTM

    universal turning machine

    * Interpreter that reads the description of any arbitrary turning machine
    * faithfully execute operations on data D precisely as M does

    δ(current state, input) = (next state, output, L|R )

    trace table - current,input,ouput,move,nextstate

    follow order
*   Dijkstra

    node(char) , visited (bool), shortest (int) previous (char

    find shortest path between node in weighted graph
*   FSM Finite State Machine

    abstract machine that consist of fixed set of possible state with a set of allowable input that change the state and possible output

    uses: design both computer programs and sequence

    * Modelling and designing
    * Program that specific language
*   Difference between mealy machine and FS automation

    Mealy machine has an output according to the input{}

    FSA doesnt have outputs
*   Mealy VS Moore

    Both determine output from present state

    mealy determine output from input
*   JSON vs XML

    * easy to understand

    Easy to develop

    * parse faster performance
    * built in function JS
    * transmit
