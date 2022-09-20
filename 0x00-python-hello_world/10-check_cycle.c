#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - a function in C that checks if a singly
 * linked list has a cycle in it
 * @list: the singly linked list
 *
 * Return: 0 if it didn't contain a cycle and 1 if it did
 */

int check_cycle(listint_t *list)
{
    listint_t *temp, *newNode;

    if(list == NULL || list->next == NULL)
        return (0);
    temp = list->next;
    newNode = list->next->next;
    while(temp && newNode && newNode->next)
    {
        if(temp == newNode)
            return (1);
        temp = temp->next;
        newNode = newNode->next->next;
    }
    return (0);
}
