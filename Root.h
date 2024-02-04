#ifndef ROOT_H //include gaurding the header file
#define ROOT_H

/*Define the error tolerance value
so the bisection iteration will stop at this point*/
#define ET 0.0001


//including necessary libraries
#include <iostream>
#include <cmath>
#include <string>

/**
 * struct stack - stack data structure 
 * for postfix notation of function
 * @term: single term of the function
 * @next: pointer to next node
*/

struct stack
{
    string term;
    stack *next;
} typedef stack;

extern stack **top = NULL;

// listing function prototypes
float bisection(float **guess, );
#endif