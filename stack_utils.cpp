#include "Root.h"

using namespace std;


/**
 * push - pushes a node to the stack
 * @term: term element of the stack data structure
*/

void push(string term){
    stack *new_node;

    new_node = malloc(sizeof(stack));
    if (new_node == NULL)
        return;

    new_node->term = term;
    if (top)
        new_node->next = *top;
    else
        new_node->next = NULL;

    top = &new_node;
}

/**
 * pop - pops a node from the stack
*/
void pop(){
    stack *temp;

    if (!top || !(*top))
        return;
    
    temp = *top;
    top = &(temp->next);
    free(temp);
}