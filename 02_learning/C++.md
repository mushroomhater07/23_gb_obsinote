# c++

![](file:///C:/Users/Shalev/AppData/Local/Temp/msohtmlclip1/01/clip\_image001.png) Need compile to execute ![](file:///C:/Users/Shalev/AppData/Local/Temp/msohtmlclip1/01/clip\_image002.png)

![](file:///C:/Users/Shalev/AppData/Local/Temp/msohtmlclip1/01/clip\_image003.png)

`.cpp` file inside the object file

Object file include machine code too Sometimes object files are api and needed to link to execute and work

![](file:///C:/Users/Shalev/AppData/Local/Temp/msohtmlclip1/01/clip\_image004.png)

we picked the open source GNU Compiler Collection, more commonly called G++ or GCC. `gcc` is a command line tool.

There are many tools available to help you compile, ranging from barebones tools, such as `g++` on Unix, to complex build systems that are integrated into IDEs like Visual Studio and Eclipse.

There is a high-level build tool called **CMake** that is fairly popular and cross-platform. CMake in and of itself, however, does not compile code. CMake results in compilation configurations. It depends on a lower-level build tool called **Make** to _manage_ compiling from source. And then Make depends on a compiler to do the actual compiling.

`./terminal`

G++ help

Help

```powershell
pwd (print working dir
chdir (cd) (change dir
dir ( print all file and folder
ls (list directory
```

To compile the program: `g++ filename.cpp -o executableName To execute the program: ``./executableName` g++ filename.cpp -o nameOfExecutableCode.sth `./nameOfExecutableCode.sth` \[to run]

## Example code

```
/*  Program:
    Written by:
    Date Written: */

#include <stdio.h>

void main{
    char x = 'a'; //single quote
    printf("hi %d \n", x); // end with ;
    
}
```

## Variable type:

* int
* float
* double
* char
