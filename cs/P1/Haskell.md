# haskell

\=> EVALUATE repl.it GHC `1: [2,3,4]` → \`\[1,2,3,4]

### Haskell

## Map

matching each element in the list generate an output list from an input list by apply in afunction to each element in the input list `functionName x = x +2` map functionName \[1...5]\`

### yellow box

## Tuple

a way to keep various mixed datatype in haskell

### Function type:  Filter function

> This function generates an output list that matches certain criteria using … if, select, where, remove\_if …

filter is the name of a higher order function that processes a data structure; typically a list in some order to produce a new data structure containing exactly those elements of the original data structure that match a given condition _filter_ is if, remove\_if, where

### Pattern matching

foldr takes three arguments: a function, an initial value and a list. client\[init] <=req, res=> server

reduce or fold is the name of a higher order function which reduce a list of values to a single value by repeatedly applying a combining function to the list value

The foldr => fold from right _combines the first element with the results of combing the rest_ The foldl => fold from left _left fold recursively combined all elmenets but the last one with the last one_

* Recursive

### List

a concatenation of a head and a tail , where head is an element in a list and tail is a list head = 1st

* return head/tail List a collection of elements of a similar type

```haskell
let listA = [1,2,3]
head listA
> 1 -- 1st element
tail listA
> [2,3]  -- remainder of the list
tail (tail listA) -- Chasing the tail = tail([2,3])
> [3]
-- Function
null(listA)
> FALSE
null[]
> TRUE
length(listA) -- number of element in list
> 3
```

Concaternation

```haskell
5 : [1,2,3] -- : for add single element into the head
> [5,1,2,3]
[5,4] ++ [1,2,3] -- ++ for add a list to front/ head
> [5,4,1,2,3] 
--immutable , the value doesnt change, only operation
-- Appending 
old ++ new
-- Prepending
new ++ old

--Concate list of string
let meal = ["fish"],["chips"],["pea"]
> ["fish","chips","pea"]
--Concate string
concat["fish", "and", "chips"]
> fishandchips

```
