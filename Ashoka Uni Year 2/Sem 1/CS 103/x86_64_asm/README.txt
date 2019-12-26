This exercise is to introduce you to basic x86-64 assembly
programming.


FILES

There are 11 files in the folder.

1. README -- This file
2. sum-prog.c -- main program file
3. sum-func.s -- assembly program to compute sum (unoptimized)
4. sum-func-opt.s -- optimizing address computation
5. sum-func-leaq.s -- example use of the leaq instruction
6. sum-func-mac.s -- Mac version of 3 
7. sum-func-mac-opt.s -- Mac version of 4
8. sum-func-mac-leaq.s -- Mac version of 5
9. test1.txt -- small test file
10. test2.txt -- medium test file
11. test3.txt -- large test file

* sum-prog.c

This file contains the "c" program that allows us to test our assembly
program. It first takes input numbers from "standard input (stdin)",
calls the sum function to compute the result, and prints the result to
"standard output (stdout)".

* sum-func.s / sum-func-mac.s

This file contains the assembly function that takes the base address
and the number of elements of an array and computes the sum of the
elements. All numbers are assumed to be 64-bit unsigned integers.

<<We filled this file in class.>>


* sum-func-opt.s / sum-func-mac-opt.s

This file uses the x86_64 base + scale*index addressing mode to
optimize the array address computation.


* sum-func-leaq.s / sum-func-mac-leaq.s

Shows an example use of the leaq instruction. Splits out the
address computation and array access into two instructions.


COMPILING THE PROGRAM

To run the program, we must first compile it. In this class, we will
use the gcc compiler that comes with most linux distributions.

For non-mac users

> gcc sum-prog.c sum-func.s -o sum

For mac users

> gcc sum-prog.c sum-func-mac.s -o sum

The above command asks gcc to compile the two files "sum-prog.c"
and "sum-func(-mac).s" and create a single executable (or
application) called "sum".


EXECUTING THE PROGRAM

> ./sum


INPUT/OUTPUT TO THE PROGRAM

The "standard input" in most systems is the keyboard. You just type in
the numbers using the keyboard. The "standard output" is the
monitor. Once you type in all the input, you can see the output in the
monitor.


TAKING INPUT FROM A FILE

Sometimes it is tedious to type the input everytime using the
keyboard. To avoid this, we can use the following trick which modifies
the "standard input" to a program to a file.

> ./sum < test1.txt

The above command executes the program "sum" as though the contents of
the file "test1.txt" were typed from the keyboard.
