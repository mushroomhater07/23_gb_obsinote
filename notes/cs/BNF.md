context free language

Regex repersent simple syntax
Context free language is complex syntaxx
RegEx 
must use BNF

notation
|     |           |     |
| --- | --------- | --- |
| l   | OR        |     |
| <>  | statement |     |
| ::= | assign to |     |


production rule
``<student> ::= <name><gender>
student must include following element
Rule state that the element on the LHS of the ::= must be replaced by one of the element of RHS
terminal element 
each element should be broken down further until a terminal is reached
``<name> ::= <first><last>
``<gender> ::= <character>
``<space> ::= ' '
``<character> ::= 'M' | 'F'``  // Terminal

parsing 
parsing is checking an input string against of BNF rule to see if it is valid 
→ ascertaining weather a given statement is valid

syntax diagram is another method of representing a context free language, the graphical equivalent of BNF

rectangle ,
 ellipse/ circle
 recursion
 boxed arrow